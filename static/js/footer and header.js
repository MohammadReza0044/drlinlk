



class header extends HTMLElement{
    connectedCallback() { 
        this.innerHTML=
      `<header>
      <div class="site-header ">
          <div class="container">
              <h1 class="site-logo">
                  <a href="/">
                      <span class="logo-first-part">دکتر</span>
                      <span class="logo-last-part">لینک</span>
                  </a>
              </h1>
              <nav>
                  <ul class="top-menu">
                      <li><a href="/">صفحه اصلی</a></li>
                      <li><a href="/about-product">معرفی محصول</a></li>
                      <li><a href="/support">درخواست مشاوره رایگان</a></li>
                      <li><a href="/blog">بلاگ</a></li>
                      <li><a href="/about-us">درباره ما</a></li>
                      <li><a href="/contact-us">ارتباط با ما</a></li>
                  </ul>
              </nav>
              <a href="/support" class="product-purchase-link" >مشاوره و خرید </a>
          </div>
      </div>
      <!--.site-header-->

      <div class="mobile-header">
          <div class="container ">
              <h1 class="mobile-header-logo">
                  <a href="/">
                      <span class="logo-first-part">دکتر</span>
                      <span class="logo-last-part">لینک</span>
                  </a>
              </h1>
              <span  class="menu-icon-res res-menu-control">
                  <svg><use xlink:href="#menu"></use></svg>
              </span>    
          </div>
      </div>
      <!-- .mobile-header -->
  </header>
  <!--header-->

`

    }
}

customElements.define('my-header', header)



