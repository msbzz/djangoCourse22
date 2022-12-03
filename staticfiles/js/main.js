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