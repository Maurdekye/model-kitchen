document.addEventListener("DOMContentLoaded", () => {
    (new MutationObserver(e => {
        // update client here
    })).observe(gradioApp(), {childList: true, subtree: true});
});