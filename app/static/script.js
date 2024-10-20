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
        apiCall(payload)
        // console.warn(payload);
    } 
    else if (!decryptForm.classList.contains('hidden')) {
        formData = new FormData(decryptForm);
        for (const [key, value] of formData.entries()) {
            dataObject[key] = value;
        }
        dataObject['isEncrypt'] = false;
        const payload = JSON.stringify(dataObject);
        apiCall(payload)
        // console.warn(payload);
    }
};

// API Calling
async function apiCall(payload) {
    showKey = document.querySelector('#showKey');
    showText = document.querySelector('#showText');
    dataModal = document.querySelector('#dataModal');
    notiBell = document.querySelector('.notiBell');
    
    try {
        const response = await fetch('/api/encrypt', {
            method:'POST',
            headers: { 'Content-Type': 'application/json' },
            body: payload
        });
        dataResponse = await response.json();
        isData = true;
        if(dataResponse.data.secret_key == undefined){
            showKey.classList.add('hidden')
        }
        showKey.value = `${dataResponse.data.secret_key}`;
        showText.value = `${dataResponse.data.text}`;
        dataModal.classList.remove('hidden');
        
    } catch (error) {
        console.error("Error in API: ", error);
    }
}
