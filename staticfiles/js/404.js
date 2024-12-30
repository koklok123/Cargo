document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.container');
    
    function createStar() {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDuration = `${Math.random() * 3 + 2}s`;
        container.appendChild(star);
        
        setTimeout(() => {
            star.remove();
        }, 5000);
    }
    
    setInterval(createStar, 100);
});