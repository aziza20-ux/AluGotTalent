// In  ../static/JS/talent_form.js

document.addEventListener('DOMContentLoaded', function() {
    
    // Select ALL elements with the class 'edit-talent-btn'
    const editButtons = document.querySelectorAll('.edit-talent-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            // 1. Get the specific ID of the talent being edited from the clicked button
            const compId = this.getAttribute('data-sponsor-id');
            
            // 2. Create and display the form using the ID
            CreateForm(compId); 
        });
    });
});


function CreateForm(compId) {
    // 3. Create elements as before
    const model = document.createElement('div');
    model.className = 'modal-backdrop';
    model.id = 'dynamic_content';

    const form_container = document.createElement('div');
    form_container.id = 'form-content';

    const newform = document.createElement('form');
    newform.className = 'my-form';
    newform.enctype = 'multipart/form-data'
    newform.method = 'POST';

 
    newform.action = `/sponsor/edit/${compId}`; 

    newform.innerHTML =  ` 
    <h2>Sponsor Details</h2>
    <label for="name" ><b>Name:</b></label>
    <input type="text" id="nameInput" name="name" placeholder="optional">
    <label for="name" ><b>companyName:</b></label>
    <input type="text" id="nameInput" name="company_name" placeholder="">

    <label for="url"><b>LinkedInURL</b></label>
    <input type="url" id="url" name="linkedIn">
    <label for="details"><b>SponsoredTalents</b></label>
    <textarea name="sponsoredtalents" id="sponsoredtalents" rows="4" cols="40"></textarea>
    <label for="name" ><b>Address:</b></label>
    <input type="text" id="nameInput" name="address" placeholder="">
    <label for="browse"><b>category:</b></label>
    <input type="text" class="form-control" id="browse" name="category" list="listbrowses">
    <datalist id="listbrowses">
        <option value="Music">
        <option value="Arts">
        <option value="Dancing">
        <option value="Event Planning">
    </datalist>
    <label for="name" ><b>Email Address:</b></label>
    <input type="text" id="nameInput" name="email_addres" placeholder="">
    <label for="name" ><b>companylogo:</b></label>
    <input type="file" id="nameInput" name="file" placeholder="">

    <button type="submit" class="btn btn-info rounded">Save</button>
    `; 
    const RemoveModel = () => {
        const removemodel = document.getElementById('dynamic_content');
        if (removemodel) {
            removemodel.remove();
        }
    };
    
    // Event listener logic remains the same
    model.addEventListener('click', (e) => {
        if (e.target === model) {
            RemoveModel();
        }
    });

    form_container.appendChild(newform);
    model.appendChild(form_container);
    document.body.appendChild(model);
}

//The previous line 'editbutton.addEventListener('click', CreateForm)' is no longer needed.