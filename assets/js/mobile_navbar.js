class mobile_navbar extends HTMLElement{
    connectedCallback() { 
        this.innerHTML=
      `<div id="mySidenav" class="sidenav">
      <div>
      <a href="" class=""> <span>بستن</span><svg><use xlink:href="#close-circle"></use></svg></a>
      <nav>
          <ul class="top-menu-side">
              <li><a href="index.html">صفحه اصلی</a></li>
              <li><a href="about-product.html">معرفی محصول</a></li>
              <li><a href="support.html">درخواست مشاوره رایگان</a></li>
              <li><a href="blog.html">بلاگ</a></li>
              <li><a href="about-us.html">درباره ما</a></li>
              <li><a href="contact-us.html">ارتباط با ما</a></li>
          </ul>
      </nav>   
      </div>     
  </div>  
  <div class="product-purchase-link-container">
      <div class="container"> 
          <a href="/survery" class=" product-purchase-link-fixed">مشاوره با ما</a>
      </div>
  </div>
`

        

    }
}

customElements.define('my-mobile-navbar', mobile_navbar)

