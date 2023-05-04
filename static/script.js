const form = document.querySelector('form');
const input = document.querySelector('input');
const ul = document.querySelector('ul');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    ul.innerHTML = '';
    const url = input.value;
    if (url) {
        fetch(`/crawl?url=${encodeURIComponent(url)}`)
            .then(response => response.text())
            .then(data => {
                ul.innerHTML = data;
            })
            .catch(error => console.error(error));
    }
});
