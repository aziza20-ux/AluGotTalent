// In your ../static/JS/talent_form.js

document.addEventListener('DOMContentLoaded', function() {
    
    // Select ALL elements with the class 'edit-talent-btn'
    const editButtons = document.querySelectorAll('.edit-talent-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            // 1. Get the specific ID of the talent being edited from the clicked button
            const talentId = this.getAttribute('data-talent-id');
            
            // 2. Create and display the form using the ID
            CreateForm(talentId); 
        });
    });
});


function CreateForm(talentId) {
    // 3. Create elements as before
    const model = document.createElement('div');
    model.className = 'modal-backdrop';
    model.id = 'dynamic_content';

    const form_container = document.createElement('div');
    form_container.id = 'form-content';

    const newform = document.createElement('form');
    newform.className = 'my-form';
    newform.method = 'POST';

 
    newform.action = `/talent/edit/${talentId}`; 

    newform.innerHTML =`
        <h2>Edit Talent</h2>
        <label for="name" ><b>Name:</b></label>
        <input type="text" id="nameInput" name="talentname" placeholder="for example singing">
        
        <label for="browse"><b>category:</b></label>
        <input class="form-control" id="browse" name="category" list="listbrowses">
        <datalist id="listbrowses">
            <option value="Music">
            <option value="Arts">
            <option value="Dancing">
            <option value="Event Planning">
        </datalist>
        
        <label for="url"><b>Talent URL</b></label>
        <input type="text" id="url" name="url">
        
        <label for="details"><b>Talent Details</b></label>
        <textarea name="details" id="detailsarea" rows="6" cols="40"></textarea>
        
        <button type="submit" class="btn btn-info rounded" id="savetalent">Save Changes</button>
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

// NOTE: The previous line 'editbutton.addEventListener('click', CreateForm)' is no longer needed.