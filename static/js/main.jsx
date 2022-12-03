 // GET SEARCH FORMS AND PAGE LINKS

let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link') 

// ENSURE SEARCH FORMS EXISTS

if(searchForm){
  for(let i=0;pageLinks.length>i;i++){
    pageLinks[i].addEventListener('click',function(e){
      e.preventDefault()
      console.log('Button clicked') 

      //GET DATA PAGE ATTRIBUTE
      let page = this.dataset.page
      console.log('Page : ',page)

      //ADD HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

      //SUBMIT FORM
      searchForm.submit()

    })
  }
}



let tags = document.getElementsByClassName('project-tag')
    
for(let i=0;tags.length >i;i++ )
{
    tags[i].addEventListener('click',(e)=>{

        let tagID = e.target.dataset.tag
        let projectID = e.target.dataset.project
        //console.log('i ==>',i) 
        //console.log('TAG ID : ',tagID)
        //console.log('PROJECT ID : ',projectID)


        fetch(`http://localhost:8000/api/remove-tag/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
               
            },
            body: JSON.stringify({ 'project': projectID,'tag':tagID })
        })

          .then(response => response.json)
          .then(data =>{
              e.target.remove()
          })



    })    

}