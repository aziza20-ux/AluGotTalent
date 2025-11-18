const addSponsorbutton = document.getElementById('addsponsor')
function CreateFormSponsor(){
    const model = document.createElement('div');
    model.className = 'modal-backdrop';
    model.id = 'dynamic_content'

    const form_container = document.createElement('div')
    form_container.id = 'form-content'

    const newform = document.createElement('form')
    newform.className = 'my-form'
    newform.method='POST'
    newform.action='/sponsor/addsponsor'
    newform.innerHTML =`
    <h2>Sponsor Details</h2>
    <label for="name" ><b>Name:</b></label>
    <input type="text" id="nameInput" name="name" placeholder="">
    <label for="name" ><b>companyName:</b></label>
    <input type="text" id="nameInput" name="companyname" placeholder="">

    <label for="url"><b>LinkedInURL</b></label>
    <input type="text" id="url" name="url">
    <label for="details"><b>SponsoredTalents</b></label>
    <textarea name="listtalents" id="listtalents" rows="4" cols="40"></textarea>
    <label for="name" ><b>Address:</b></label>
    <input type="text" id="nameInput" name="address" placeholder="">
    <label for="name" ><b>Email Address:</b></label>
    <input type="text" id="nameInput" name="email" placeholder="">

    <button type="submit" class="btn btn-info rounded">Save</button>
    `
    const RemoveModel = () =>{
        const removemodel = document.getElementById('dynamic_content')
        if (removemodel) {
            removemodel.remove();
    }
    }
    model.addEventListener('click', (e) => {
        // Check if the target clicked is the backdrop itself, not a child element
        if (e.target === model) {
            RemoveModel();
        }
    })

    form_container.appendChild(newform)
    model.appendChild(form_container);
    document.body.appendChild(model);
}

addSponsorbutton.addEventListener('click',CreateFormSponsor)