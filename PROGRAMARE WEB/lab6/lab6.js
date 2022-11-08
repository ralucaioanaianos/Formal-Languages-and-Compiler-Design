const highlightRe = /<span class="highlight">(.*?)<\/span>/g;
const highlightHtml = '<span class="highlight">$1</span>';

document.ondblclick = function () {
    const word = window.getSelection().toString();
    console.log(word);
    let txt = $('#txt').html().replace(highlightRe,'$1');
    if(word !== '') {
        txt = txt.replace(new RegExp('(' + word + ')', 'gi'), highlightHtml);
    }
    $('#txt').html(txt);
};

// regex flags:
// g = all occurrences are selected
// i = case-insensitive


