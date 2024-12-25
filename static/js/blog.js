
document.addEventListener("DOMContentLoaded",function (event) {
    console.log("This is blog.js");
    let sc=document.createElement('script')
    sc.setAttribute('src','https://cdn.tiny.cloud/1/8mwviczrd802u1ue1sacsm80835tbf6k9pjsvtcxwuck4aa9/tinymce/7/tinymce.min.js');
    document.head.appendChild(sc);
    sc.onload=()=>{
   // tinymce.init({
      //  selector:'#id_content'
    //}

    //);
const fetchApi = import(
  "https://unpkg.com/@microsoft/fetch-event-source@2.0.1/lib/esm/index.js"
).then((module) => module.fetchEventSource);

// This example stores the OpenAI API key in the client side integration. This is not recommended for any purpose.
// Instead, an alternate method for retrieving the API key should be used.
const openai_api_key = "<INSERT_OPENAI_API_KEY_HERE>";

const useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

tinymce.init({
  selector: '#id_content',
  plugins: 'importword exportword exportpdf ai preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link math media mediaembed codesample table charmap pagebreak nonbreaking anchor tableofcontents insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker editimage help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable footnotes mergetags autocorrect typography advtemplate markdown revisionhistory',

  mobile: {
    plugins: 'ai preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link math media mediaembed codesample table charmap pagebreak nonbreaking anchor tableofcontents insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable footnotes mergetags autocorrect typography advtemplate',
  },
  menu: {
    tc: {
      title: 'Comments',
      items: 'addcomment showcomments deleteallconversations'
    }
  },
  menubar: 'file edit view insert format tools table tc help',
  toolbar: "undo redo | importword exportword exportpdf | revisionhistory | aidialog aishortcuts | blocks fontsizeinput | bold italic | align numlist bullist | link image | table math media pageembed | lineheight  outdent indent | strikethrough forecolor backcolor formatpainter removeformat | charmap emoticons checklist | code fullscreen preview | save print | pagebreak anchor codesample footnotes mergetags | addtemplate inserttemplate | addcomment showcomments | ltr rtl casechange | spellcheckdialog a11ycheck", // Note: if a toolbar item requires a plugin, the item will not present in the toolbar if the plugin is not also loaded.


});

}
});