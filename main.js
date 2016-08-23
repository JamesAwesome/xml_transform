var dragDrop = require('drag-drop/buffer');
var colorbox = require('jquery-colorbox');

dragDrop('textarea#xml', function (files) {
  files.forEach(function (file) {
    $('textarea#xml').val(file.toString())
  })
})

dragDrop('textarea#xsl', function (files) {
  files.forEach(function (file) {
    $('textarea#xsl').val(file.toString())
  })
})

$('textarea#xml').on('dragover',  function() {
  $('textarea#xml').css({ 'background-color': '#e6ffe6', 'border': '5px #00e600 dashed' })
})

$('textarea#xml').on('dragleave', function() {
  $('textarea#xml').removeAttr( 'style' );
})

$('textarea#xml').on('drop', function() {
  $('textarea#xml').removeAttr( 'style' );
})

$('textarea#xsl').on('dragover',  function() {
  $('textarea#xsl').css({ 'background-color': '#e6ffe6', 'border': '5px #00e600 dashed' })
})

$('textarea#xsl').on('dragleave', function() {
  $('textarea#xsl').removeAttr( 'style' );
})

$('textarea#xsl').on('drop', function() {
  $('textarea#xsl').removeAttr( 'style' );
})

$(document).ready(function() {
    var xml = document.getElementById('inline_content')
    if (xml !== null) {
      $('#inline_content').show()
      $.colorbox({width:800, inline: true, href: '#inline_content', open:true, onClosed:function() { $('#inline_content').hide()} });
    }
})

$("#btn-save").click( function() {
  var text = $("textarea#output_xml").val();
  var blob = new Blob([text], {type: "text/xml;charset=utf-8"});
  saveAs(blob, "transformed.xml");
});

