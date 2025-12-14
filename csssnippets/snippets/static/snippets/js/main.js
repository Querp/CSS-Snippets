const navE = document.querySelector('nav');
const navToggleE = document.getElementById('nav-toggle');

// Nav Toggle
navToggleE.addEventListener('click', () => {
    navE.classList.toggle('show')
});


// Link Click => Close Nav
navE.addEventListener('click', (event) => {
    const w = window.innerWidth;
    console.log('width', w);


    const link = event.target.closest('a');
    if (link && window.innerWidth < 1200) {
        console.log('clicked a link');
        navE.classList.remove('show');
    }
})

// Copy Buttons EventHandlers
function initCopyButtonEventHandlers() {
    const buttons = document.querySelectorAll('#snippets .copy-button');

    buttons.forEach(buttonE => {
        const snippetE = buttonE.closest('.details');
        const codeE = snippetE.querySelector('.code-preview');

        buttonE.addEventListener('click', (e) => {
            e.stopPropagation(); // prevent parent details click from firing
            navigator.clipboard.writeText(codeE.textContent.trim())
                .then(() => {
                    console.log(`Copied: \n${codeE.textContent.trim()}`);
                    buttonE.classList.add('copied');
                    codeE.classList.add('copied');

                    setTimeout(() => {
                        buttonE.classList.remove('copied');
                        codeE.classList.remove('copied');
                    }, 2000);
                })
                .catch(err => console.error('Failed to copy:', err));
        });
    });
}

initCopyButtonEventHandlers();
