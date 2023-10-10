let searchForm = document.getElementById('search');

let pageLinks = document.querySelectorAll('.page-link');

if(searchForm){
    for(let i=0; pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault()

            let page = this.dataset.page;
            searchForm.innerHTML += `<input value=${page} name='page' type='hidden'>`;
            searchForm.submit();
        })
    }
}

let p  = document.getElementsByClassName('pink');

for(let i=0; i<p.length; i++){
    p[i].addEventListener('mouseover', function (event){
    event.target.style.color = '#e598a8'
    event.target.style.fontWeight = '500'
    });
    p[i].addEventListener('mouseout', function (event){
    event.target.style.color = '#526e6e'
    event.target.style.fontWeight = '300'
    });
}

let s  = document.getElementsByClassName('pink-second');

for(let i=0; i<s.length; i++){
    s[i].addEventListener('mouseover', function (event){
    event.target.style.color = '#ffffff'
    event.target.style.fontWeight = '500'
    });
    s[i].addEventListener('mouseout', function (event){
    event.target.style.color = '#2d4242'
    event.target.style.fontWeight = '300'
    });
}



