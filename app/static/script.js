const encryptForm = document.querySelector('#encryptForm');
const decryptForm = document.querySelector('#decryptForm');
const alertToastr = document.querySelector('#alertToastr');
const msgToastr = document.querySelector('#msgToastr');
const mainLoader = document.querySelector('#mainLoader');
mainData = {}

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

// Copy to Clipboard
function copyToClipboard(encrypt){
    
    try{
        if (encrypt.length >12){
            navigator.clipboard.writeText(`->Encrypted message: ${mainData.data.text} ->Secret key: ${mainData.data.secret_key}`);
        } else {
            navigator.clipboard.writeText(mainData.data.text);
        }
        msgToastr.innerText = "Successfully copied!";
        alertToastr.style.background = 'green'
            alertToastr.style.right = '16px';

            setTimeout(() => {
                alertToastr.style.right = '-100%'
            }, 6000);
    } catch (err){
        console.error("Error in copy", err)
    } 
}

// API Calling
async function apiCall(payload) {
    mainLoader.style.display = 'flex';

    showKey = document.querySelector('#showKey');
    isKey = document.querySelector('#isKey');
    showText = document.querySelector('#showText');
    dataModal = document.querySelector('#dataModal');
    notiBell = document.querySelector('#notiBell');
    
    try {
        const response = await fetch('/api/encrypt', {
            method:'POST',
            headers: { 'Content-Type': 'application/json' },
            body: payload
        });
        dataResponse = await response.json();
        mainData = dataResponse;
        // isData = true;

        if (dataResponse.error){
            msgToastr.innerText = dataResponse.error;
            alertToastr.style.background = 'red'
            alertToastr.style.right = '16px';

            setTimeout(() => {
                alertToastr.style.right = '-100%'
            }, 6000);
        } else {
            if(dataResponse.data.secret_key == undefined){
                showKey.classList.add('hidden');
                isKey.classList.add('hidden');
            }
            showKey.value = `${dataResponse.data.secret_key}`;
            showText.value = `${dataResponse.data.text}`;
            dataModal.classList.remove('hidden');
        }

        mainLoader.style.display = 'none';
        
    } catch (error) {
        console.error("Error in API: ", error);
        mainLoader.style.display = 'none';
    }
}

setTimeout(() => {
    mainLoader.style.display = 'none';
}, 1500);