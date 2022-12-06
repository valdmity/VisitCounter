function getCookie(name) {
	let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : '-1';
}
if (getCookie('id') === '-1'){
    document.cookie = "id=0";
}
let url = 'http://192.168.3.5:8000/' + getCookie('id');

fetch(url)
    .then(response => response.text()
        .then(v => document.cookie = "id=" + v));