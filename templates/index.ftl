<#include "header.ftl">
	<#include "menu.ftl">

      <div class="row-fluid marketing">
        <div class="span9">
          <h2>Publications</h2>
          <ul>
          	<#list posts as post>
          		<#if (post.status == "published")>
          			<li><p>${post.date?string("yyyy-MM-dd")}: <a href="/${post.uri}">${post.title}</a></p></li>
          		</#if>
          	</#list>
          </ul>
        </div>        
      </div>

      <hr>

<#include "footer.ftl">
