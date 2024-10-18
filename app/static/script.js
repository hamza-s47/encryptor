const encryptForm = document.querySelector('#encryptForm');
const decryptForm = document.querySelector('#decryptForm');

const btnToggle = () => {
    const encryptToggle = document.querySelector('#encryptToggle');
    const decryptToggle = document.querySelector('#decryptToggle');

    if (encryptToggle.checked) {
        decryptForm.classList.add('hidden');
        encryptForm.classList.remove('hidden');

    } else if (decryptToggle.checked) {
        encryptForm.classList.add('hidden');
        decryptForm.classList.remove('hidden');
    }
};

// Add event listeners to radio buttons
document.querySelectorAll('input[name="e2d-radio"]').forEach(radio => {
    radio.addEventListener('change', btnToggle);
});

// Initial call to set the correct form on page load
btnToggle();

const submitForm = (event) => {
    event.preventDefault();

    let formData;
    const dataObject = {};
    
    if (!encryptForm.classList.contains('hidden')) {
        formData = new FormData(encryptForm);
        for (const [key, value] of formData.entries()) {
            dataObject[key] = value;
        }
        dataObject['isEncrypt'] = true;
        const payload = JSON.stringify(dataObject);
        console.warn(payload);
    } 
    else if (!decryptForm.classList.contains('hidden')) {
        formData = new FormData(decryptForm);
        for (const [key, value] of formData.entries()) {
            dataObject[key] = value;
        }
        dataObject['isEncrypt'] = false;
        const payload = JSON.stringify(dataObject);
        console.warn(payload);
    }
};