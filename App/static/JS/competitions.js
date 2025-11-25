const addcompetitionsbutton = document.getElementById('addcompetition')
function CreateFormCompetitions(){
    const model = document.createElement('div');
    model.className = 'modal-backdrop';
    model.id = 'dynamic_content'

    const form_container = document.createElement('div')
    form_container.id = 'form-content'

    const newform = document.createElement('form');
    newform.className = 'my-form';
    newform.method ='POST';
    newform.action = '/comp/addcomp'
    
    newform.innerHTML =`
    <h2>Competition Details</h2>
    <label for="name" ><b>Title:</b></label>
    <input type="text" id="nameInput" name="title" placeholder="">
    <label for="details"><b>competition details</b></label>
    <textarea name="details" id="detailsarea" rows="4" cols="40"></textarea>
    <label for="browse"><b>category:</b></label>
    <input class="form-control" id="browse" name="category" list="listbrowses">
    <datalist id="listbrowses">
        <option value="Music">
        <option value="Arts">
        <option value="Dancing">
        <option value="Event Planning">
    </datalist>
    <label for="name" ><b>Deadline:</b></label>
    <input type="date" id="nameInput" name="deadline" placeholder="">
    <label for="name" ><b>apply link:</b></label>
    <input type="url" id="nameInput" name="appylink" placeholder="https://....">

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
   // newform.addEventListener('submit',function(event){
     //   event.preventDefault();
       // RemoveModel();
    //});
    form_container.appendChild(newform)
    model.appendChild(form_container);
    document.body.appendChild(model);
}

addcompetitionsbutton.addEventListener('click',CreateFormCompetitions)