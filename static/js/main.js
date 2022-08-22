jQuery(document).ready(function($) {
    var url = window.location.href; 
    $(".top-menu li a , .site-footer-menu a ,.top-menu-side a ").removeClass('active');
    $(".top-menu li a , .site-footer-menu a ,.top-menu-side a ").each(function() {
        if(url == (this.href)) { 
            $(this).addClass("active");
        }
    });
  

    /*timeline(about-us page)*/

    $('.timeline-container').css('width' , $('.timeline').outerWidth()/2-37);
    var first_container = $('.timeline-container:first-of-type').outerHeight()/2;
    var last_container = $('.timeline-container:last-of-type').outerHeight()/2;
    var curheight = $('.timeline-after').outerHeight();
    $('.timeline-after').css(
        {
            "height": curheight-(last_container+first_container) , 
            'top' : first_container
        }
    );

   
    /*
    *customers slider(main page)
    */ 
    var customers_swiper = new Swiper('.customers-slider', {
        slidesPerView: 2.3,
        centeredSlides: true,
        paginationClickable: true,
        loop: true,
        spaceBetween: 16, 
        slideToClickedSlide: true,
        pagination: {
          el: '.customer-slider-pag',
          clickable: true,
        },
        navigation: {
            nextEl: '.customer-swiper-button-next',
            prevEl: '.customer-swiper-button-prev',
        },
       
        breakpoints: {
            576: {
                spaceBetween: 16,
                slidesPerView: 3.9,
                centeredSlides: false,
                centeredSlidesBounds: false,
            },
            768: {
                spaceBetween: 41,
                slidesPerView: 4,
                centeredSlides: false,
                centeredSlidesBounds: false,
            },
            1400: {
                spaceBetween: 24,
                slidesPerView: 5,

            },
        }
    });
    var top_offset = $('.slide-customer-name').css('height');
    $('.slide-customer-logo').css('height' , $('.slide-customer-logo').outerWidth() );
    $('.customer-swiper-button-next , .customer-swiper-button-prev ').css('top' , $('.slide-customer-logo').outerWidth() /2 +10);  


    /*
    *latest-aticles slider (main page)
    */ 
    var latest_articles_swiper = new Swiper('.latest-articles-slider', {
        slidesPerView:1.35,
        centeredSlides: true,
        paginationClickable: true,
        loop: true,
        spaceBetween: 20,
        slideToClickedSlide: true,
        navigation: {
            nextEl: '.larticles-swiper-button-next',
            prevEl: '.larticles-swiper-button-prev',
        },
        breakpoints: {
    
        450: {
            spaceBetween: 24,
            slidesPerView: 1.9,
        },
        576: {
            spaceBetween: 16,
            slidesPerView: 2.2,
        },
        700: {
            spaceBetween: 16,
            slidesPerView: 2.75,
        },
        1400: {
            spaceBetween: 80,
            slidesPerView: 3,

        },
        1200: {
            spaceBetween: 24,
            slidesPerView: 3,
            centeredSlides: false,
        }
       
        }
    });

    /**
     * accordian product panels (products page)
     */
    $('.p-panel-title').each(function(){
        $(this).on('click' , function(e){
            e.preventDefault();
            $(this).toggleClass('p-panel-active');
            this_arrow =  $(this).find('svg');
            this_arrow.toggleClass('ap-rotate-svg');
            panel_content = $(this).parent().find('.p-panel-content');
            panel_content.slideToggle('slow');        
        });    
    
     });


   

   


    
    
    /**
     * Mobile menu
    */
    $(document).on('click','.res-menu-control',function(e){
        e.preventDefault(); 
        if($(this).hasClass('closebtn')) {
            closeNav();
        }
        else {
            openNav();
        }
    });  


    

    
    


   

    /**
     * show/hide header
     */
    var lastScrollTop = 0;
    $(window).scroll(function() {
        var currentScrollTop = $(this).scrollTop();
        toScroll = $(document).height() - $(window).height() - 100;

        if (currentScrollTop >600) {
            if (window.matchMedia('(max-width: 900px)').matches) {
                $('.product-purchase-link-container').css('opacity' ,'1');
            } else {
                $('.product-purchase-link').css('opacity' ,'1');
            }
        }
        if(currentScrollTop == 0 ||   currentScrollTop > toScroll ) {
            if($('.site-service').length >0) {
                if (window.matchMedia('(max-width: 900px)').matches) {
                    $('.product-purchase-link-container').css('opacity' ,'0');
                } else {
                    $('.product-purchase-link').css('opacity' ,'0');
                }    
            }     
        }
        if (currentScrollTop > lastScrollTop && currentScrollTop> 400) {
            if ( $('.mobile-header').css('display') != 'none') {
                $('.mobile-header').addClass('hide-header');
            }
            if ($('.site-header').css('display') != 'none'){
                 $(' .site-header').addClass('hide-header');
            }
          
           
        } else {
            if ( $('.mobile-header').css('display') != 'none') {
                $('.mobile-header').removeClass('hide-header');
            }
            if ($('.site-header').css('display') != 'none') {
                $(' .site-header').removeClass('hide-header');
            }
          

        }
        lastScrollTop = currentScrollTop;
    });

    /**
     * styles
     */
    $('.i-article-big .i-article-detail').css('width' , $('.i-article-big').width());
  
});
    
function change_value_onclick (elem , tagetimputname) {
    new_val = elem.attr('data-inputval');
    tagetimputname.val(new_val);
}
function openNav() {
    target_width = $(window).width() + "px";
    n_target_width = (-1 * $(window).width()) + "px";
    $("#mySidenav").css('width', target_width);
    $("#site_wrap").css('transform', 'translateX(' + n_target_width + ')');
    $("body").css('overflow-y', 'hidden');
    $("body").css('overflow-x', 'hidden');
    $("html").css('overflow-y', 'hidden');
    $("html").css('overflow-x', 'hidden');
} 
function closeNav() {
    $("#mySidenav").css('width', "0px");
    $("#site_wrap").css('transform', "translateX(0px)");
    $("body").css('overflow-y', 'auto');
    $("body").css('overflow-x', 'auto');
    $("html").css('overflow-y', 'auto');
    $("html").css('overflow-x', 'auto');
}

function showTab(n) {
    var x = $(".ms-tab").eq(n);   
    x.css('display' , 'flex');
    if(n==0) {
        $("#msurvey_prevBtn").css('display' , 'none');
    }
    else {
        if (n == ($(".ms-tab").length )) {
                $('#survey_form_multistep').css('display', 'none');
                $('#survey_form_multistep').fadeOut();
                $('.s-page-title').text('تشکر');
                $('.finish-tab').addClass('finish-tab-show').fadeIn();
        }
        else {
            $("#msurvey_nextBtn").css('display' , 'block');
        } 
    }
  
    $('.step').removeClass('active');
    x.addClass('active');
}


  