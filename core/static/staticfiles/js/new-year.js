// ... existing code ...

// Christmas Tree
function createChristmasTree() {
    const container = document.querySelector('.container');
    const tree = document.createElement('div');
    tree.className = 'christmas-tree';
    container.appendChild(tree);

    for (let i = 0; i < 5; i++) {
        const branch = document.createElement('div');
        branch.className = 'branch';
        tree.appendChild(branch);
    }

    const trunk = document.createElement('div');
    trunk.className = 'trunk';
    tree.appendChild(trunk);
}

// Snowballs
function createSnowballs() {
    const container = document.querySelector('.container');
    for (let i = 0; i < 5; i++) {
        const snowball = document.createElement('div');
        snowball.className = 'snowball';
        snowball.style.left = `${Math.random() * 100}%`;
        snowball.style.animationDuration = `${Math.random() * 2 + 2}s`;
        snowball.style.animationDelay = `${Math.random() * 2}s`;
        container.appendChild(snowball);
    }
}

// Initialize animations
createSnowflakes();
createStars();
createChristmasTree();
createSnowballs();