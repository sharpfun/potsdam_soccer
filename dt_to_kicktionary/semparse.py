


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>potsdam_soccer/semparse.py at master · KaiserKlayton/potsdam_soccer</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="KaiserKlayton/potsdam_soccer" name="twitter:title" /><meta content="Contribute to potsdam_soccer development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/10909774?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/10909774?v=3&amp;s=400" property="og:image" /><meta content="KaiserKlayton/potsdam_soccer" property="og:title" /><meta content="https://github.com/KaiserKlayton/potsdam_soccer" property="og:url" /><meta content="Contribute to potsdam_soccer development by creating an account on GitHub." property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTAyMDg1NjU6YWUzNzhjNjBkMTU3NDM3YzUxYTVhZjYxM2I0Zjg4ZWE6NzY4YTg4OGMyYWFmODQwMDUxMWQzZTRkMzkxNDZkZTFiMTE2NGVjMGQ0ZDg2NGViMDQ1OGM4MTM5MWYyODBhNw==--2fe074b2a444e415f250ecc5f28b59338121a01e">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="8D59A9C5:1A4E:1ECFF01:556EE4B2" name="octolytics-dimension-request_id" /><meta content="10208565" name="octolytics-actor-id" /><meta content="jimk1n" name="octolytics-actor-login" /><meta content="78a54db8b7c0d410e8f13e14f84f49d850689634538507aafde4f27f4301206a" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
    <meta class="js-ga-set" name="dimension2" content="Header v3">
    <meta name="is-dotcom" content="true">
      <meta name="hostname" content="github.com">
    <meta name="user-login" content="jimk1n">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="wAD35HN6bn+1wvpZTEPTW68SOFjFUX2ooQdw+faosAxOZ0mM3bwh+uMyKoRl8dx6Vjo7uysl86iZS4R1hGdYxA==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github/index-6967b378b26829cc5a2ea2ad4209ff0af50f2a65057962219dc9dcf8942683f0.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2/index-73bfe123ff406f4bf8959a28667410beaac1485e71c92d4725a3d7afc45fc4c5.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="afea9b2859824308c0a0b3687f45e4b1">

      
  <meta name="description" content="Contribute to potsdam_soccer development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/KaiserKlayton/potsdam_soccer git https://github.com/KaiserKlayton/potsdam_soccer.git">

  <meta content="10909774" name="octolytics-dimension-user_id" /><meta content="KaiserKlayton" name="octolytics-dimension-user_login" /><meta content="35207693" name="octolytics-dimension-repository_id" /><meta content="KaiserKlayton/potsdam_soccer" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="35155223" name="octolytics-dimension-repository_parent_id" /><meta content="sharpfun/potsdam_soccer" name="octolytics-dimension-repository_parent_nwo" /><meta content="35155223" name="octolytics-dimension-repository_network_root_id" /><meta content="sharpfun/potsdam_soccer" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/KaiserKlayton/potsdam_soccer/commits/master.atom" rel="alternate" title="Recent Commits to potsdam_soccer:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public fork page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/KaiserKlayton/potsdam_soccer/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item explore">
            <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
          </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
            </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
            </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
          </li>
      </ul>

      
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/jimk1n" data-ga-click="Header, go to profile, text:username">
      <img alt="@jimk1n" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/10208565?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">jimk1n</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="/new" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu">
        
<li>
  <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
</li>
<li>
  <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
</li>



      </ul>
    </div>
  </li>

  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:jimk1n"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
          <span class="mail-status all-read"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Nv/gt5qlKS6YY8YbPX17agL3ZmCAm3Tx7aDt012yGSghlEY3pLfnCoJ6oK9ReBIARwh3JBpTyed3xkKrq/BHiQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>



    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">

        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mpa9EeaqT+brfkQvwHSiLFQCoE/waUW6p2y66m5dz33MJASQRwqHJiquRj3hP843gvtm15rni4ph7tyIyeWepw==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="35207693" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/KaiserKlayton/potsdam_soccer/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>
        <a class="social-count js-social-count" href="/KaiserKlayton/potsdam_soccer/watchers">
          1
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fXRLcq/1hBbYSE/z7wCJs083PUbknrN9kTOGlDl4VoQPbKdB7p6SNbhd5qYashfT8L5LZ+ahFSa0CWSMeZl8XQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar KaiserKlayton/potsdam_soccer"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/KaiserKlayton/potsdam_soccer/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="APxHqerkAgog3SgBD5ZI0z5QsJS9+yvGAr5Mobmn/3yoyHlytAnh83HOdvDgoug6z//ynxc5bXw5CtEOiTZz5Q==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star KaiserKlayton/potsdam_soccer"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/KaiserKlayton/potsdam_soccer/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/fork" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="tMzxfREpYkcTFJQ5SF0ik7263eF7f+dKNGbZSOj5W8sQPOG//9mI3dMUNEp82tC9se3lFbfZgEUJQY2nfDfq8A==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of KaiserKlayton/potsdam_soccer to your account"
                aria-label="Fork your own copy of KaiserKlayton/potsdam_soccer to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/KaiserKlayton/potsdam_soccer/network" class="social-count">3</a>
</form>        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author"><a href="/KaiserKlayton" class="url fn" itemprop="url" rel="author"><span itemprop="title">KaiserKlayton</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/KaiserKlayton/potsdam_soccer" data-pjax="#js-repo-pjax-container">potsdam_soccer</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/sharpfun/potsdam_soccer">sharpfun/potsdam_soccer</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/KaiserKlayton/potsdam_soccer/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/KaiserKlayton/potsdam_soccer" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /KaiserKlayton/potsdam_soccer">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/KaiserKlayton/potsdam_soccer/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /KaiserKlayton/potsdam_soccer/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/KaiserKlayton/potsdam_soccer/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /KaiserKlayton/potsdam_soccer/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/KaiserKlayton/potsdam_soccer/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /KaiserKlayton/potsdam_soccer/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/KaiserKlayton/potsdam_soccer/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /KaiserKlayton/potsdam_soccer/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="js-clone-url clone-url "
  data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/KaiserKlayton/potsdam_soccer.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url open"
  data-protocol-type="ssh">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:KaiserKlayton/potsdam_soccer.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/KaiserKlayton/potsdam_soccer" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<div class="clone-options">You can clone with
  <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Ov1MQDEaKsvtoPyW/xgvUNLVhN8ElrxMlWnWXf4+tyDzro00VV8oY0K504i1f2AIyc+ySmLXt3QF2+TmVy8Giw==" /></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form>, <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Rliqv9xdI397Axjn+8YX9XaOYNo+nvUMyiW49HRQ2wrEMLtisOb4Vm8ygelID5wiY9uTw1og0duss1ZYjPu2eA==" /></div><button class="btn-link js-clone-selector" data-protocol="ssh" type="submit">SSH</button></form>, or <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="NH0JQecwF/0RNQu/P3MEWq7ToiBNYdNEi0YRJ3gZ/UdPYoDgGaz/P16ecEaL7KGLKkXi3iJfbM2RK2aj15/FLA==" /></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</div>


  <a href="github-windows://openRepo/https://github.com/KaiserKlayton/potsdam_soccer" class="btn btn-sm sidebar-button" title="Save KaiserKlayton/potsdam_soccer to your computer and use it in GitHub Desktop." aria-label="Save KaiserKlayton/potsdam_soccer to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/KaiserKlayton/potsdam_soccer/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of KaiserKlayton/potsdam_soccer as a zip file"
                   title="Download the contents of KaiserKlayton/potsdam_soccer as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/KaiserKlayton/potsdam_soccer/blob/09e77145f30ac232a6af59390f5119edac86c967/dt_to_kicktionary/semparse.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:2c851ec014d4a06853b1285b287330ab -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/KaiserKlayton/potsdam_soccer/blob/master/dt_to_kicktionary/semparse.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/KaiserKlayton/potsdam_soccer/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/KaiserKlayton/potsdam_soccer" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">potsdam_soccer</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/KaiserKlayton/potsdam_soccer/tree/master/dt_to_kicktionary" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">dt_to_kicktionary</span></a></span><span class="separator">/</span><strong class="final-path">semparse.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@KaiserKlayton" class="avatar" height="24" src="https://avatars2.githubusercontent.com/u/10909774?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/KaiserKlayton" rel="author">KaiserKlayton</a></span>
        <time datetime="2015-06-01T11:37:54Z" is="relative-time">Jun 1, 2015</time>
        <div class="commit-title">
            <a href="/KaiserKlayton/potsdam_soccer/commit/57294456958a43fc064460f845307183e664ef1c" class="message" data-pjax="true" title="added some verbnet functionality">added some verbnet functionality</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>2</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="KaiserKlayton" href="/KaiserKlayton/potsdam_soccer/commits/master/dt_to_kicktionary/semparse.py?author=KaiserKlayton"><img alt="@KaiserKlayton" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/10909774?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jimk1n" href="/KaiserKlayton/potsdam_soccer/commits/master/dt_to_kicktionary/semparse.py?author=jimk1n"><img alt="@jimk1n" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/10208565?v=3&amp;s=40" width="20" /> </a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@KaiserKlayton" height="24" src="https://avatars2.githubusercontent.com/u/10909774?v=3&amp;s=48" width="24" />
            <a href="/KaiserKlayton">KaiserKlayton</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@jimk1n" height="24" src="https://avatars0.githubusercontent.com/u/10208565?v=3&amp;s=48" width="24" />
            <a href="/jimk1n">jimk1n</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/KaiserKlayton/potsdam_soccer/raw/master/dt_to_kicktionary/semparse.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/KaiserKlayton/potsdam_soccer/blame/master/dt_to_kicktionary/semparse.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/KaiserKlayton/potsdam_soccer/commits/master/dt_to_kicktionary/semparse.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/KaiserKlayton/potsdam_soccer?branch=master&amp;filepath=dt_to_kicktionary%2Fsemparse.py"
           aria-label="Open this file in GitHub for Windows"
           data-ga-click="Repository, open with desktop, type:windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/edit/master/dt_to_kicktionary/semparse.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="G9yTCJhm4OrOu09183HeCAUUnUn0aB4bPhwIZ2XJlHgZ5nK5ImtLDZV7rJVme6004zcON7k6wIIPehK3IUpB9w==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Edit the file in your fork of this project" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/KaiserKlayton/potsdam_soccer/delete/master/dt_to_kicktionary/semparse.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Ol0eGBtClLhzEElQOTfc0qkcOJd54kvgKBHzkC9nyGE9728+SG/SkwNrv3ZwH+sFvCpIulRO5e6OyPC90uQL7w==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Delete this file in your fork of this project" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        100 lines (87 sloc)
        <span class="file-info-divider"></span>
      5.041 kB
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Master script. Identifies Kicktionary and Verbnet matches of ticker sentences.</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># 1. Look up roots in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># 2. Look up root-object pairs in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># 3. Look up roots in Verbnet via Verbnet frame in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       This means: Can we match the tree root to a Verbnet verb, get it&#39;s </span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       Verbnet frame, and then match *this* frame to Kicktionary? In this way, </span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       we have an *indirect* root--&gt;kictionary relation VIA the frame.</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># 4. Look up roots via frame siblings in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       This means: Can we mateh the tree root to a Verbnet verb, iterate over</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       it&#39;s siblings, and then match *this* sibling to Kicktionary? In this</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#       way, we have an *indirect* root--&gt;kictionary relation VIA the sibling.</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> __future__ <span class="pl-k">import</span> division</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> optparse</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> bs4 <span class="pl-k">import</span> BeautifulSoup</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> nltk</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ticker <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> kicktionary <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> verbnet <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">lookup</span>(<span class="pl-smi">kicktionary</span>, <span class="pl-smi">verbnet</span>, <span class="pl-smi">ticker</span>, <span class="pl-smi">verbose</span>):</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Looking up tree roots in Kicktionary...<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Looking up root-object pairs in Kicktionary...<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Looking up tree roots in Verbnet...<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Looking up tree roots (via Verbnet) in Kicktionary...<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> tree <span class="pl-k">in</span> ticker:</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        possibleLUs <span class="pl-k">=</span> [lu <span class="pl-k">for</span> lu <span class="pl-k">in</span> kicktionary <span class="pl-k">if</span> lu.lemma <span class="pl-k">==</span> tree.root]</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># 4-Step Classification:</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># 1. Look up root in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">                tree.lexical_unit <span class="pl-k">=</span> possibleLUs[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Tree <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree.tree_id) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> root matches Kicktionary lexical unit: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tree.lexical_unit.lemma</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># how to determine??</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Tree <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree.tree_id) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> root with possible LUs: <span class="pl-pds">&quot;</span></span>, possibleLUs</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># 2. Look up root-object pairs in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># Find the arguments of the root.</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">            root_id <span class="pl-k">=</span> [<span class="pl-c1">int</span>(node.node_id) <span class="pl-k">for</span> node <span class="pl-k">in</span> tree.nodes <span class="pl-k">if</span> <span class="pl-c1">int</span>(node.head) <span class="pl-k">==</span> <span class="pl-c1">0</span>][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">            arguments <span class="pl-k">=</span> [node <span class="pl-k">for</span> node <span class="pl-k">in</span> tree.nodes <span class="pl-k">if</span> <span class="pl-c1">int</span>(node.head) <span class="pl-k">==</span> root_id <span class="pl-k">and</span> node.type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>OBJ<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># Look for OBJ in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">            possibleLUs <span class="pl-k">=</span> [lu <span class="pl-k">for</span> lu <span class="pl-k">in</span> kicktionary <span class="pl-k">if</span> lu.lemma <span class="pl-k">==</span> arguments[<span class="pl-c1">0</span>].lemma] <span class="pl-k">if</span> arguments <span class="pl-k">else</span> []</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">                    tree.lexical_unit <span class="pl-k">=</span> possibleLUs[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Tree <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree.tree_id) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> root matches Kicktionary lexical unit: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tree.lexical_unit.lemma</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"># how to determine??</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Tree <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree.tree_id) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> root with possible LUs: <span class="pl-pds">&quot;</span></span>, possibleLUs</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># 3. Look up roots in Verbnet via Verbnet frame in Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># a. Root--&gt;Verbnet.Verb--&gt;Verbnet.Frame--&gt;Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># b. Root--&gt; Verbnet.Verb--&gt;Verbnet.Sibling--&gt;Kicktionary.</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> vb <span class="pl-k">in</span> verbnet:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> vb.lemma <span class="pl-k">==</span> tree.root:</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">                        possibleLUs <span class="pl-k">=</span> [lu <span class="pl-k">for</span> lu <span class="pl-k">in</span> kicktionary <span class="pl-k">if</span> lu.lemma <span class="pl-k">==</span> vb.frame]</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">if</span> <span class="pl-c1">len</span>(possibleLUs) <span class="pl-k">==</span> <span class="pl-c1">1</span>: </td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">                                tree.lexical_unit <span class="pl-k">=</span> possibleLUs[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">                                <span class="pl-k">if</span> verbose: <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Tree <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree.tree_id) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> root matches (via Verbnet frame) Kicktionary unit: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tree.lexical_unit.lemma</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">                            <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">                                <span class="pl-k">pass</span> <span class="pl-c"># &lt;-- how to determine??</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"> <span class="pl-c">#                       else: </span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"> <span class="pl-c">#                           tree.lexical_unit == vb</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"> <span class="pl-c">#                           if verbose: print &quot;Tree &quot; + str(tree.tree_id) + &quot; root matches Verbnet lexical unit: &quot; + tree.lexical_unit.lemma</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> ticker</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    parser <span class="pl-k">=</span> optparse.OptionParser()</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">    parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>--kicktionary<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>kicktionary<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>location of kicktionary xml file<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>../data/kicktionary.xml<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>--ticker<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>ticker<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>location of parsed ticker conll file<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>../data/p2.parsed<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>--verbose<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>verbose<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>print helpful messages about the progress<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>--language<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>language<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>language of tickers (en or de)<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>en<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">## will need to add verbnet XML file(s) at some point, maybe a complete folder</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>--verbnet<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>verbnet<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>location of folder with verbnet xml files<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>../data/verbnet<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    (options, args) <span class="pl-k">=</span> parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    verbose <span class="pl-k">=</span> options.verbose</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    language <span class="pl-k">=</span> options.language</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#raw_input()</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    ticker <span class="pl-k">=</span> read_ticker(options.ticker, verbose, language)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#raw_input()</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    kicktionary <span class="pl-k">=</span> read_kicktionary(options.kicktionary, verbose, language)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#raw_input()</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    verbnet <span class="pl-k">=</span> read_verbnet(options.verbnet, verbose, language)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    matches <span class="pl-k">=</span> lookup(kicktionary, verbnet, ticker, verbose)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#print matches</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    main()</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.05959s from github-fe117-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-447ce66a36506ebddc8e84b4e32a77f6062f3d3482e77dd21a77a01f0643ad98.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github/index-d03b4728b2a35c0b94963f035c99d5fd32f59fb9ace2ab651b9a4267e1d394df.js"></script>
      
      
  </body>
</html>

