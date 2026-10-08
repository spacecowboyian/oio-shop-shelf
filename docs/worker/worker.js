/**
 * Shop shelf display state — a Cloudflare Worker.
 *
 * The display polls outward and never accepts a connection, so this is the only
 * piece that has to be reachable from the internet. It stores one small record per
 * room and nothing else:
 *
 *   GET  /state?room=<id>                       -> {manual, page, rev, at}
 *   POST /goto?room=<id>&page=N[&manual=slug]   -> same, with rev bumped
 *
 * Deploy (free tier is far more than enough):
 *   npm create cloudflare@latest shelf-state -- --type=hello-world
 *   # replace src/index.js with this file
 *   npx wrangler kv namespace create SHELF
 *   # add the returned id to wrangler.toml as the SHELF binding, then:
 *   npx wrangler deploy
 *
 * Then put the deployed origin in docs/config.js as stateBase.
 *
 * A room id is the only credential: anyone holding it can change what the screen
 * shows. Use something unguessable, and treat it as a secret rather than a name.
 */

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store", ...CORS },
  });

// Keep room ids to something that cannot collide or be used to probe other keys.
const validRoom = (r) => !!r && /^[A-Za-z0-9_-]{8,64}$/.test(r);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const room = url.searchParams.get("room");

    if (request.method === "OPTIONS") return new Response(null, { headers: CORS });

    if (!validRoom(room)) {
      return json({ error: "room must be 8-64 chars of [A-Za-z0-9_-]" }, 400);
    }
    const key = `room:${room}`;

    if (url.pathname === "/state" && request.method === "GET") {
      const cur = await env.SHELF.get(key, "json");
      return json(cur || { manual: null, page: 1, rev: 0, at: null });
    }

    if (url.pathname === "/goto" && (request.method === "POST" || request.method === "GET")) {
      const page = parseInt(url.searchParams.get("page") || "", 10);
      if (!Number.isInteger(page) || page < 1 || page > 10000) {
        return json({ error: "page must be an integer between 1 and 10000" }, 400);
      }
      const cur = (await env.SHELF.get(key, "json")) || { rev: 0 };
      const next = {
        manual: url.searchParams.get("manual") || cur.manual || null,
        page,
        rev: (cur.rev || 0) + 1,          // the display moves only when rev changes
        at: new Date().toISOString(),
      };
      // Expire idle rooms rather than keeping state for a display nobody uses.
      await env.SHELF.put(key, JSON.stringify(next), { expirationTtl: 60 * 60 * 24 * 30 });
      return json(next);
    }

    return json({ error: "not found" }, 404);
  },
};
