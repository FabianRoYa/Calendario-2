function toggleIframe() {
    var iframe = document.getElementById("miIframe");
    if (iframe.getAttribute("disabled") === "true") {
        iframe.removeAttribute("disabled");
    } else {
        iframe.setAttribute("disabled", "true");
    }
}
