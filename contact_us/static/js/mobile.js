
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

