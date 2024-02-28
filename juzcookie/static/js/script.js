// adjust viewport size based on viewport
document.addEventListener("load", (event) => {
    function adjustFontSize() {
        // obtain viewport width 
        const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        // set rem default to 24px
        const baseFontSize = 24;
        const scaleFactor = viewportWidth / 1280;

        // calculate how much to resize base font size
        const adjustedSize = scaleFactor * baseFontSize

        // add base font into HTML element
        document.documentElement.style.fontSize = adjustedSize + 'px';
    }

    // call the function when  page is loaded or resized
    window.addEventListener("resize", adjustFontSize);

    adjustFontSize()
    }
)