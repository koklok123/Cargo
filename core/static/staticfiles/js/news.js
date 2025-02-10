document.addEventListener('DOMContentLoaded', function() {
    // Sample news data (in a real scenario, this would come from a backend API)
    const newsData = [
        {
            id: 1,
            title: "Shipping Industry Transformation in 2024",
            excerpt: "Exploring the latest technological innovations revolutionizing global logistics and maritime transportation.",
            date: "April 15, 2024",
            author: "Jane Smith",
            image: "images/cargo_sea_1.jpg",
            category: "Industry Trends"
        },
        {
            id: 2,
            title: "Sustainable Shipping: Green Technologies",
            excerpt: "How modern cargo companies are reducing their carbon footprint and embracing eco-friendly solutions.",
            date: "March 22, 2024",
            author: "John Doe",
            image: "images/cargo_ship_2.jpg",
            category: "Sustainability"
        },
        {
            id: 3,
            title: "AI in Logistics: Revolutionizing Supply Chains",
            excerpt: "The impact of artificial intelligence on optimizing routes, predicting demand, and enhancing efficiency in cargo operations.",
            date: "February 10, 2024",
            author: "Emily Chen",
            image: "images/ai_logistics.jpg",
            category: "Technology"
        },
        {
            id: 4,
            title: "Global Trade Shifts: New Routes and Opportunities",
            excerpt: "Analyzing emerging trade patterns and their implications for the shipping industry in a post-pandemic world.",
            date: "January 5, 2024",
            author: "Michael Johnson",
            image: "images/global_trade.jpg",
            category: "Market Analysis"
        }
    ];

    const itemsPerPage = 2;
    let currentPage = 1;

    function renderNewsItems(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;
        const newsListContainer = document.getElementById('news-list');
        newsListContainer.innerHTML = '';

        for (let i = startIndex; i < endIndex && i < newsData.length; i++) {
            const news = newsData[i];
            const newsItem = document.createElement('div');
            newsItem.className = 'col-lg-6 mb-5';
            newsItem.innerHTML = `
                <div class="news-item">
                    <div class="image-container">
                        <img src="${news.image}" alt="${news.title}" class="img-fluid">
                        <span class="category">${news.category}</span>
                    </div>
                    <h2 class="news-title"><a href="single.html?id=${news.id}">${news.title}</a></h2>
                    <div class="news-meta">
                        <span class="date">${news.date}</span>
                        <span class="author">by ${news.author}</span>
                    </div>
                    <p>${news.excerpt}</p>
                    <a href="single.html?id=${news.id}" class="read-more">Read More</a>
                </div>
            `;
            newsListContainer.appendChild(newsItem);
        }
    }

    function renderPagination() {
        const totalPages = Math.ceil(newsData.length / itemsPerPage);
        const paginationContainer = document.getElementById('page-numbers');
        paginationContainer.innerHTML = '';

        for (let i = 1; i <= totalPages; i++) {
            const pageNumber = document.createElement('span');
            pageNumber.textContent = i;
            pageNumber.className = i === currentPage ? 'active' : '';
            pageNumber.addEventListener('click', () => {
                currentPage = i;
                renderNewsItems(currentPage);
                renderPagination();
            });
            paginationContainer.appendChild(pageNumber);
        }

        document.getElementById('prev-page').style.display = currentPage > 1 ? 'inline' : 'none';
        document.getElementById('next-page').style.display = currentPage < totalPages ? 'inline' : 'none';
    }

    document.getElementById('prev-page').addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            renderNewsItems(currentPage);
            renderPagination();
        }
    });

    document.getElementById('next-page').addEventListener('click', () => {
        const totalPages = Math.ceil(newsData.length / itemsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            renderNewsItems(currentPage);
            renderPagination();
        }
    });

    // Initial render
    renderNewsItems(currentPage);
    renderPagination();
});