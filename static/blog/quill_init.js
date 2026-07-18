document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.querySelector('#id_content');
    if (!textarea) return;

    textarea.style.display = 'none';

    const editorDiv = document.createElement('div');
    editorDiv.style.height = '300px';
    editorDiv.style.backgroundColor = 'white';
    textarea.parentNode.insertBefore(editorDiv, textarea);

    const quill = new Quill(editorDiv, {
        theme: 'snow',
    });

    quill.root.innerHTML = textarea.value;

    quill.on('text-change', function () {
        textarea.value = quill.root.innerHTML;
    });

    textarea.closest('form').addEventListener('submit', function () {
        textarea.value = quill.root.innerHTML;
    });
});