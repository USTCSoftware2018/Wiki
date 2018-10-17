$(document).ready(function () {
        $('.container').height($(window).height()-$('#menu').height() - 12)       
        $('.wide').height($(window).height()-$('#menu').height() - 30)
        $('#leftnav').height($(window).height() - $('#menu').height() - 100)
$('.ui.menu .ui.dropdown').dropdown({
        on: 'hover'
      });
$('.ui.menu a.item')
        .on('click', function() {
          $(this)
            .addClass('active')
            .siblings()
            .removeClass('active')
          ;
        })
      ;
    })
