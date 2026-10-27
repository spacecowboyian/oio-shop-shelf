// Hosted reader settings. Edit, commit, and GitHub Pages serves it.
//
// stateBase: origin of the state endpoint that lets a link (or a chat) move the page
//            on a display that is already showing. Leave "" and the reader still
//            works — it just only responds to its own ?page= and the remote.
//            See docs/worker/worker.js for a deployable implementation.
// room:      which display the state belongs to. Make it unguessable: anyone with
//            the string can change what your screen shows.
window.SHELF_CONFIG = {
  stateBase: "",
  room: "",
};
