
class footer extends HTMLElement{
    connectedCallback() { 
        this.innerHTML=
      `    <footer class="site-footer">
      <div class="container  site-footer-content">
          <a href="/" class="site-footer-logo">
              <span class="logo-first-part">دکتر</span>
              <span class="logo-last-part">لینک</span>
          </a>
          <div class="site-footer-contact-info">
              <span class="footer-contact-phone col-xxl-3"><span>تلفن تماس: </span><span>۰۲۱ - ۴۴۵۵۶۶۷۷</span></span>
              <span class="footer-contact-time"><span>ساعات پاسخگویی:</span><span>از <span class="time-contain">۸ صبح تا 9 شب</span>  به غیر از روز های تعطیل</span></span>
          </div>
          <div class="site-footer-detail">
              <div class="site-footer-menu col-xxl-3">
                  <!-- <h5 class="footer-det-title">دکتر لینک</h5> -->
                  <nav>
                      <ul>
                          <li><a href='/'>دکتر لینک</a></li>
                          <li><a href="contact-us">درباره ما</a></li>
                          <li><a href="rules.html">قوانین و مقررات </a></li>
                          <li><a href="privacy.html">حریم خصوصی</a></li>
                      </ul>
                  </nav>
              </div>

              <div  class="site-footer-text col-xxl-5">
                  <h5 class="footer-det-title">دکتر لینک ، سیستم مدیریت مراکز درمانی</h5>
                  <p>سیستم هوشمند مدیریت مطب، کلینیک و بیمارستان دکتر لینک با قدرت تمام و اطمینان در دنیای پزشکی همواره در تلاش است تا با آخرین دستاورد های دنیای تکنولوژی IT مسیر روشنی در جهت مدیریت آسان و حرفه ای برای مدیران و پزشکان مراکز درمانی ایجاد کند. این سیستم هوشمند در مدیریت مطب، کلینیک و بیمارستان میتواند نقش مهمی را برای جذب بیمار و وفادارسازی مراجعین ایفا کند.</p>
              </div>
              <div class="site-footer-enamad col-xxl-2">
                  <a href="#"><img src="assets/images/enamad1.png" /></a>
                  <a href="#"><img src="assets/images/enamad2.png" /></a>
              </div>
          </div>
          <!--.site-footer-detail-->

          <div class="footer-copyright">
              <p>تمامی حقوق این سایت مربوط به <a href="/"> دکتر لینک </a>می باشد.  </p>
              <div class="social-media-links">
                  <a href="#" title ="linkedin">
                      <svg class="drlink-icon">
                          <use xlink:href="#linkedin"></use>
                      </svg>
                  </a>
                  <a href="#" title ="whatsapp">
                      <svg class="drlink-icon">
                          <use xlink:href="#whatsapp"></use>
                      </svg>
                  </a>
                  <a href="#" title ="instagram">
                      <svg class="drlink-icon">
                          <use xlink:href="#instagram"></use>
                      </svg>
                  </a>
                  <a href="#" title ="twitter">
                      <svg class="drlink-icon">
                          <use xlink:href="#twitter"></use>
                      </svg>
                  </a>
                  <a href="#" title="telegram">
                      <svg class="drlink-icon">
                          <use xlink:href="#telegram"></use>
                      </svg>
                  </a>
              </div>
          </div>
          <!--.footer-copyright-->
      </div>
      <!--.site-footer-content-->
  </footer>
  <!--.site-footer-->
  </div>
`

        

    }
}

customElements.define('my-footer', footer)



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
                      <li><a href="about-product.html">معرفی محصول</a></li>
                      <li><a href="/support">درخواست مشاوره رایگان</a></li>
                      <li><a href="/blog">بلاگ</a></li>
                      <li><a href="about-us.html">درباره ما</a></li>
                      <li><a href="/contact-us">ارتباط با ما</a></li>
                  </ul>
              </nav>
              <a href="/survery" class="product-purchase-link" >مشاوره با ما</a>
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
`

        

    }
}

customElements.define('my-header', header)



