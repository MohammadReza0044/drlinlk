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


    /*
    * support form (support page)
    */ 
    num_options = $('#req_date option');
    if(num_options.length > 0) {
        $('#req_date').attr ('size' , num_options.length)
    }
    $(document).on('submit','form#customer_support_form',function(e){
        e.preventDefault();
        //ajax code
        $('#support_form_modal').modal('show');
        $('.site-header').css('display', 'none');
        $('.modal').addClass('modal-centerd');
    }) ;  

    /**
     * survay form
     */
    $(document).on('change click','form#survey_form input',function(){
        if($(this).hasClass('invalid-input')  ){
            $(this).next().fadeOut();
            $(this).next().remove();
            $(this).removeClass('invalid-input');
        }
        else if ($(this).hasClass('invalid-radio-input')) {
            $('.range-age-content').next().fadeOut();
            $('.range-age-content').next().remove();
            $('.range-age-content input').removeClass('invalid-radio-input');
        }
    });


    $(document).on('submit','form#survey_form',function(e){
        e.preventDefault();
        error = false;
        $('.input-validation-message').remove();
        form_values = $(this).find('input[type=text]');
        form_values.removeClass('invalid-input');
        form_values.each(function() {
            if($(this).hasClass('required-field') && $(this).val() == '' ) {
                error = true;
                $(this).addClass('invalid-input');
                message = '<p class="input-validation-message">لطفا این فیلد  را تکمیل کنید</p>';
                $('<p class="input-validation-message">لطفا این فیلد را تکمیل کنید.</p>').insertAfter($(this));
            }  
        });
        var radioValue = $("input[name='req_range_age']:checked").val();
        if(!radioValue && $("input[name='req_range_age']").hasClass('required-field')){
            error = true;
            $("input[name='req_range_age']").addClass('invalid-radio-input');
            $('<p class="input-validation-message">یکی از گزینه ها را انتخاب کنید.</p>').insertAfter($('.range-age-content'));
        }
        if(error){
            $('.input-validation-message').fadeIn();
        }
        else {
            //ajax code
            $('#survey_form_modal').modal('show');
            $('.modal').addClass ('modal-centerd');
            $('.site-header').css('display' , 'none');
        }
    });
    $(document).on('click',' .modal-close',function(e){
        e.preventDefault();
        $('.modal').removeClass ('modal-centerd');
        $($(this).attr('data-mid')).modal('hide');
        $('.site-header').removeAttr('style');
    });

    /*
    * support option-time & time 
    */
    $(document).on('click','.option-box',function(e){
        e.preventDefault();
        target_input = ($(this).hasClass('time-option')) ? $('input[name=req_time]'):$('input[name=req_date]');
        custom_class =  ($(this).hasClass('time-option')) ? '.time-option' : '.date-option';
        selected = $(this).hasClass('option-selected') ? false :true;
        $(custom_class).removeClass('option-selected' ,{duration:1000});
        if(selected) {
            $(this).addClass('option-selected' , {duration:1000});
            change_value_onclick ($(this) ,  target_input);
        }
        else {
            target_input.val('');
        }
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
     * multi-step survey form
     */
    var currentTab = 0; 
    var def_prev_val = -1 ;
    var def_next_val = 1;
    showTab(currentTab); 
    $(document).on('click','#msurvey_nextBtn , #msurvey_prevBtn , #submit_step_form',function(e){
        e.preventDefault();
        n = (($(this).attr('id')== 'msurvey_nextBtn') || ($(this).attr('id')== 'submit_step_form') ) ?  def_next_val :  def_prev_val ;
        // if (n == 1) return false;
        $(".ms-tab").eq(currentTab).css('display' , 'none');;
        currentTab = currentTab + n;
        showTab(currentTab);   
    });
    $(document).on('click','.start-survey',function(e){
        e.preventDefault();
        $(this).parent().parent().fadeOut();
        $('#survey_form_multistep').fadeIn();
    });

    
    /*end:multi-step survey form */

     /**
     * article_send_comment form
     */
    $('.palceholder').click(function() {
        $(this).siblings('input').focus();
      });
      $('.form-control').focus(function() {
        $(this).siblings('.palceholder').hide();
      });
      $('.form-control').blur(function() {
        var $this = $(this);
        if ($this.val().length == 0)
          $(this).siblings('.palceholder').show();
    });
    $('.form-control').blur();

    $(document).on('submit','form.comment-form',function(e){
        e.preventDefault();
        error = false;
        var required_fields = [];
        $("form.comment-form input , form.comment-form textarea").each(function() {
            if($(this).hasClass('required-field')) {
                required_fields.push($(this).attr('name'));
            }
        });
        var values = $(this).serializeArray();
        $.each(values, function(index, value){  
            if(value['value'] =='' && $.inArray( value['name'], required_fields) !== -1 ){
                error = true;
                // return false; 
            }
        });
        if(error){
            $('#fail_comm_form_modal').modal('show');
            $('.site-header').css('display', 'none');
            $('#fail_comm_form_modal').css('z-index', '2000');
            $('#success_comm_form_modal').css('z-index', '1000');
 
        }
        else {
            //ajax code
            $('#success_comm_form_modal').modal('show');
            $('#fail_comm_form_modal').css('z-index', '1000');
            $('#success_comm_form_modal').css('z-index', '2000');
            $('.site-header').css('display', 'none');
        }
        $('.modal').addClass ('modal-centerd');
    });
    /*end:article_send_comment form */


    /**
     * like article 
    */
    $(document).on('click','.like-num',function(e){
        e.preventDefault();
        var cur_value = parseInt($(this).find('span').text());
        var new_value = ($(this).hasClass('add-like')) ? cur_value-1 : cur_value+1 ;
        $(this).toggleClass('add-like');
        $(this).find('span').text(new_value);
    });
    /*end:like article */

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


  