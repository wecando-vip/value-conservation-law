/* ============================================================
   通用底部 · 许可与声明  (Shared Footer · License & Disclaimer)
   财情倍增的价值守恒定律 / The Law of Value Conservation
   站点：https://wecando.vip/value-conservation-law/
   用法：在文章 </body> 前引入 <script src="../assets/footer.js"></script>
   说明：单点维护，所有文章共享；根据 <html lang> 自动切换中/英文案
   ============================================================ */
(function () {
  'use strict';
  if (document.getElementById('vcl-footer')) return;

  var lang = (document.documentElement.lang || '').toLowerCase();
  var isForeign = lang.indexOf('en') === 0 ||
                  lang.indexOf('es') === 0 ||
                  lang.indexOf('fr') === 0;

  var orgHref = 'https://wecando.vip/';

  /* ---- 文库导航（可选）----
     页面在引入本脚本前定义 window.VCL_NAV：
       VCL_NAV = { back:{href,title}, home:{href,title}, prev:{href,title}, next:{href,title} }
     有定义才渲染导航条；未定义则仅输出许可与声明。 */
  var nav = window.VCL_NAV;
  var navHtml = '';
  if (nav) {
    var mk = function (key, label, arrow) {
      var o = nav[key];
      if (!o) return '';
      return '<a class="vcl-nav-link' + (key === 'next' ? ' vcl-nav-next' : '') + '" href="' + o.href + '" title="' + o.title + '">' + (arrow === 'l' ? '← ' : '') + label + (arrow === 'r' ? ' →' : '') + '</a>';
    };
    navHtml = '<div class="vcl-nav">' +
      mk('back', '返回文库', 'l') +
      mk('home', '首页', '') +
      mk('prev', '上一篇', 'l') +
      mk('next', '下一篇', 'r') +
      '</div>';
  }

  var html = navHtml + (isForeign
    ? '<div class="vcl-footer-title">License &amp; Disclaimer</div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">Content License</span>' +
      '<p>This document is licensed under the CC BY-NC 4.0 (Attribution-NonCommercial 4.0 International) license. Anyone is free to quote, translate, adapt and share it, provided that attribution is given, this license notice is retained, and it is not used for commercial purposes.</p></div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">Copyright</span>' +
      '<p>The theoretical framework and content are owned by <a href="' + orgHref + '" target="_blank" rel="noopener">Econ-Sentiment Twin Think Tank (财情双生智库)</a> and the contributing authors, including Yi Hezhong.</p></div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">Disclaimer</span>' +
      '<p>This project is a discussion of ideas and methodology. It does not constitute investment advice or policy advice. Please cite the source when referencing.</p></div>'
    : '<div class="vcl-footer-title">许可与声明</div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">内容许可</span>' +
      '<p>本文档内容遵循 CC BY-NC 4.0（署名-非商业性使用 4.0 国际）许可协议，任何人可以自由引用、翻译、改编、传播，但不得用于商业目的，且必须标注署名并保留许可声明。</p></div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">版权归属</span>' +
      '<p>理论体系与文档内容版权归<a href="' + orgHref + '" target="_blank" rel="noopener">财情双生智库（Econ-Sentiment Twin Think Tank）</a>及 易和中 等相关作者所有。</p></div>' +
      '<div class="vcl-footer-item"><span class="vcl-footer-tag">免责声明</span>' +
      '<p>本项目内容为思想理论与方法探讨，不构成任何投资建议或政策建议；引用请注明出处。</p></div>');

  var css = '#vcl-footer{display:block;margin:44px auto 0;max-width:960px;padding:0 20px 40px;box-sizing:border-box}' +
    '#vcl-footer .vcl-footer-inner{border-top:3px solid #a67c2e;background:#faf9f6;border-radius:0 0 8px 8px;padding:22px 26px 20px;box-shadow:0 2px 14px rgba(22,50,79,.08)}' +
    '#vcl-footer .vcl-nav{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 16px;padding-bottom:14px;border-bottom:1px dashed #e2cfa3}' +
    '#vcl-footer .vcl-nav-link{display:inline-block;padding:5px 14px;border-radius:999px;font-size:13px;font-weight:700;text-decoration:none;color:#16324f;background:#fff;border:1px solid #d8d4c8;transition:all .2s ease;box-shadow:0 1px 3px rgba(20,30,40,.05)}' +
    '#vcl-footer .vcl-nav-link:hover{background:#16324f;color:#fff;border-color:#16324f;text-decoration:none}' +
    '#vcl-footer .vcl-nav-link.vcl-nav-next{margin-left:auto}' +
    '@media (max-width:640px){#vcl-footer .vcl-nav-link.vcl-nav-next{margin-left:0}}' +
    '#vcl-footer .vcl-footer-title{font-size:15px;font-weight:700;color:#16324f;margin:0 0 12px;letter-spacing:.04em}' +
    '#vcl-footer .vcl-footer-item{display:flex;gap:10px;margin:0 0 10px;font-size:13px;line-height:1.7;color:#3d4a5a}' +
    '#vcl-footer .vcl-footer-item:last-child{margin-bottom:0}' +
    '#vcl-footer .vcl-footer-tag{flex:none;background:#16324f;color:#fff;font-size:12px;font-weight:700;padding:1px 10px;border-radius:999px;height:22px;line-height:22px;margin-top:1px}' +
    '#vcl-footer .vcl-footer-item p{margin:0;color:#3d4a5a}' +
    '#vcl-footer a{color:#a67c2e;font-weight:600;text-decoration:underline;text-underline-offset:2px}' +
    '@media (max-width:640px){#vcl-footer .vcl-footer-item{flex-direction:column;gap:4px}}' +
    '@media print{#vcl-footer{display:none}}';

  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  var foot = document.createElement('footer');
  foot.id = 'vcl-footer';
  foot.setAttribute('role', 'contentinfo');
  foot.innerHTML = '<div class="vcl-footer-inner">' + html + '</div>';
  document.body.appendChild(foot);

  // 51la 网站统计（新版 SDK；innerHTML 中的 <script> 不会执行，须动态注入）
  if (!document.getElementById('LA_COLLECT')) {
    var laScript = document.createElement('script');
    laScript.id = 'LA_COLLECT';
    laScript.charset = 'UTF-8';
    laScript.src = '//sdk.51.la/js-sdk-pro.min.js';
    laScript.onload = function () {
      try { if (typeof LA !== 'undefined') LA.init({ id: 'KkGSSRhpvS9sEcmA', ck: 'KkGSSRhpvS9sEcmA' }); } catch (e) {}
    };
    document.body.appendChild(laScript);
  }
})();
