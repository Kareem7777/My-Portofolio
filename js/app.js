var sections = document.querySelectorAll('.section')
var sectBtns = document.querySelectorAll('.controls')
var sectBtn = document.querySelectorAll('.control')
var allSections = document.querySelector('.main-content')

function PageTransition() {
  for (let i = 0; i < sectBtn.length; i++) {
    sectBtn[i].addEventListener('click', function(){
      let currentBtn = document.querySelectorAll('.active-btn');
      currentBtn[0].className = currentBtn[0].className.replace('active-btn', '')
      this.className += ' active-btn'
    })
  }
  // Sections Active Class
  allSections.addEventListener('click', (e) => {
    var id = e.target.dataset;
    if (id) {
      // Remove selected from the other btns
      sectBtns.forEach((btn) => {
        btn.classList.remove('active')
      })
      e.target.classList.add('active')
      // Hide other sections
      sections.forEach((section) => {
        section.classList.remove('active')
      })
      var element = document.getElementById(id['id'])
      element.classList.add('active')
    }
  } )
}
PageTransition()
