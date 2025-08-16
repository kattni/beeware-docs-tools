// get the list of all highlight code blocks
const highlights = document.querySelectorAll("div.highlight pre code");
// console.log(highlights)

highlights.forEach((pre) => {
    const copyButtonDiv = document.createElement("div");
    const copiedTextDiv = document.createElement("div");
    copyButtonDiv.classList.add("copy-button")
    copiedTextDiv.classList.add("copied-text")
    const copyButtonSVG = document.createElementNS("http://www.w3.org/2000/svg","svg")
    const copyButtonSVGPath = document.createElementNS("http://www.w3.org/2000/svg","path")
    copyButtonSVGPath.setAttribute("d","M208 0H332.1c12.7 0 24.9 5.1 33.9 14.1l67.9 67.9c9 9 14.1 21.2 14.1 33.9V336c0 26.5-21.5 48-48 48H208c-26.5 0-48-21.5-48-48V48c0-26.5 21.5-48 48-48zM48 128h80v64H64V448H256V416h64v48c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V176c0-26.5 21.5-48 48-48z")
    copyButtonSVG.setAttribute("viewBox","0 0 448 512")
    copyButtonSVG.appendChild(copyButtonSVGPath)
    copyButtonDiv.appendChild(copyButtonSVG)
    copyButtonSVG.classList.add("copy-icon")
    copyButtonDiv.addEventListener("click", handleCopyClick);
    copyButtonDiv.prepend(copiedTextDiv);
    pre.prepend(copyButtonDiv);
});

const exclude = ["div.copy-button", "div.copied-text", "span.gp", "span.go"]

function filterText(target, exclude) {
    const clone = target.cloneNode(true);  // clone as to not modify the live DOM
    if (exclude) {
        clone.querySelectorAll(exclude).forEach(node => node.remove());
    }
    let content = clone.innerText
    if (content.startsWith(" ")) {
        const initial = content.replace(/^ /gm, "")
        content = initial.trim()
        return content
    }
    return content;
}

function handleCopyClick(evt) {
    const code_node = evt.target.parentElement.parentElement.parentElement
    navigator.clipboard.writeText(filterText(code_node, exclude));
    this.classList.add("copy-button-copied")
    this.classList.remove("copy-button")
    this.firstChild.textContent = "Copied! "
    setTimeout(() => {
        this.classList.remove("copy-button-copied")
        this.classList.add("copy-button")
        this.firstChild.textContent = ""
    }, 2000);
}
