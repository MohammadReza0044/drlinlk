
class footer extends HTMLElement{
    connectedCallback() { 
        this.innerHTML=
      ` <footer class="site-footer">
      <div class="container  site-footer-content">
          <a href="index.html" class="site-footer-logo">
              <span class="logo-first-part">دکتر</span>
              <span class="logo-last-part">لینک</span>
          </a>
          <div class="site-footer-contact-info">
              <span class="footer-contact-phone col-xxl-3"><span>تلفن تماس: </span><span>۰۲۱۲۲۰۶۷۶۳۵</span> <span>تماس فوری: ۰۹۱۲۰۰۴۴۸۲۴</span></span>
                              <span class="footer-contact-time"><span>ساعات پاسخگویی: </span><span>از <span class="time-contain">۸ صبح تا ۸ شب</span> و در روز های تعطیل با موبایل تماس بگیرید</span></span>
          </div>
          <div class="site-footer-detail">
              <div class="site-footer-menu col-xxl-3">
                  <!-- <h5 class="footer-det-title">دکتر لینک</h5> -->
                  <nav>
                      <ul>
                          <li><a href="index.html">دکتر لینک</a></li>
                          <li><a href="about-us.html">درباره ما</a></li>
                          <li><a href="rules.html">قوانین و مقررات </a></li>
                          <li><a href="privacy.html">حریم خصوصی</a></li>
                      </ul>
                  </nav>
              </div>

              <div  class="site-footer-text col-xxl-5">
                  <h5 class="footer-det-title">دکتر لینک، مدیریت هوشمند کلینیک</h5>
                  <p>سیستم جامع و یکپارچه مدیریت دکتر لینک، یک سیستم حرفه ای تشکیل شده از کانال های ارتباطی هوشمند و یکپارچه جهت مدیریت سریع و با کیفیت در راستای جذب و وفادار سازی درمانجو می باشد، این سیستم به مدیران ارشد کمک میکند تا در مسیر رشد بهترین تصمیمات مدیریتی را اتخاذ و با اطمینان خاطر برای آینده کلینیک خود برنامه ریزی کنند، دکتر لینک با افتخار از سال ۱۳۸۹ در این مسیر قدم نهاد.</p>
              </div>
              <div class="site-footer-enamad col-xxl-2">
                  <a href="#"><img src="assets/images/enamad1.png" /></a>
                  <a href="#"><img src="assets/images/enamad2.png" /></a>
              </div>
          </div>
          <!--.site-footer-detail-->

          <div class="footer-copyright">
              <p>تمامی حقوق این سایت مربوط به <a href="index.html">دکتر لینک </a>می باشد.  </p>
              <div class="social-media-links">
                  <a href="#" title ="linkedin">
                      <svg class="drlink-icon">
                          <use xlink:href="#linkedin"></use>
                      </svg>
                  </a>
                  <a href="https://www.linkedin.com/company/13298799/" title ="whatsapp">
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
  <!--site_wrap-->
  <div id="mySidenav" class="sidenav">
      <div>
      <a href="#" class="closebtn res-menu-control"> <span>بستن</span><svg><use xlink:href="#close-circle"></use></svg></a>
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
          <a href="#" class=" product-purchase-link-fixed">مشاوره با ما</a>
      </div>
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
                  <a href="index.html">
                      <span class="logo-first-part">دکتر</span>
                      <span class="logo-last-part">لینک</span>
                  </a>
              </h1>
              <nav>
                  <ul class="top-menu">
                      <li><a href="index.html">صفحه اصلی</a></li>
                      <li><a href="about-product.html">معرفی محصول</a></li>
                      <li><a href="support.html">درخواست مشاوره رایگان</a></li>
                      <li><a href="blog.html">بلاگ</a></li>
                      <li><a href="about-us.html">درباره ما</a></li>
                      <li><a href="contact-us.html">ارتباط با ما</a></li>
                  </ul>
              </nav>
              <a href="#" class="product-purchase-link" >مشاوره با ما</a>
          </div>
      </div>
      <!--.site-header-->

      <div class="mobile-header">
          <div class="container ">
              <h1 class="mobile-header-logo">
                  <a href="index.html">
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



