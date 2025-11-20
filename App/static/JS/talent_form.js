const addtalentbutton = document.getElementById('addtalent')


function CreateForm(){
    const model = document.createElement('div');
    model.className = 'modal-backdrop';
    model.id = 'dynamic_content'

    const form_container = document.createElement('div')
    form_container.id = 'form-content'

    const newform = document.createElement('form')
    newform.className = 'my-form';
    newform.method = 'POST';
    newform.action = '/talent/addtalent';

    newform.innerHTML =`
    <h2>Talent Details</h2>
    <label for="name" ><b>Name:</b></label>
    <input type="text" id="nameInput" name="talentname" placeholder="for example singing">
    <label for="email" ><b>email:</b></label>
    <input type="email" id="email" name="email" placeholder="your work email">
    <label for="phone" ><b>phone number:</b></label>
    <input type="text" id="phone" name="phone" placeholder="active number">
    <label for="insta" ><b>instagram:</b></label>
    <input type="url" id="insta" name="inst" placeholder="instagram link">
    <label for="tiktok" ><b>tiktok:</b></label>
    <input type="url" id="tiktok" name="tiktok" placeholder="tiktok link">
    <label for="face" ><b>facebook:</b></label>
    <input type="url" id="face" name="facebook" placeholder="facebook link">
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
    <label for="details"><b>TalentDetails</b></label>
    <textarea name="details" id="detailsarea" name="details" rows="6" cols="40"></textarea>
    <button type="submit" class="btn btn-info rounded" id="savetalent">Save</button>
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
    //newform.addEventListener('submit',function(event){
    //    event.preventDefault();
     //   RemoveModel();
    //});
    form_container.appendChild(newform)
    model.appendChild(form_container);
    document.body.appendChild(model);
}

addtalentbutton.addEventListener('click',CreateForm)

