# `boardwalkd serve`

<div class="full-width" id="cmd-help-text">
<pre>

                                                                                                              
 <span style="color: #808000; text-decoration-color: #808000">Usage:</span> <span style="font-weight: bold">boardwalkd serve</span> [<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">OPTIONS</span>]                                                                            
                                                                                                              
 Runs the server                                                                                              
                                                                                                              
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────╮</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--auth-expire-days</span>              <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">FLOAT                   </span>  The number of days login tokens and user API  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              keys are valid before they expire             <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">[default: 14]                                </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--auth-method</span>                   <span style="color: #bfbf7f; text-decoration-color: #bfbf7f; font-weight: bold">[</span><span style="color: #808000; text-decoration-color: #808000; font-weight: bold">anonymous</span><span style="color: #bfbf7f; text-decoration-color: #bfbf7f; font-weight: bold">|</span><span style="color: #808000; text-decoration-color: #808000; font-weight: bold">google_oauth</span><span style="color: #bfbf7f; text-decoration-color: #bfbf7f; font-weight: bold">]</span>  Enables an authentication method for the web  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              UI. The API always requires authentication,   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              however without this option configured a      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              predictable anonymous user will be used. The  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              method is supplied as a string argument. The  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              BOARDWALK_SECRET environment variable must be <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              set for any method to work except for         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              &#x27;anonymous&#x27;; it is the key used to sign       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              secure strings, such as auth cookies and API  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              keys                                          <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Available auth methods:                       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              anonymous                                     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              All requests are performed as an &#x27;anonymous&#x27;  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              default user                                  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              google_oauth                                  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Uses Google Oauth2 to identify users by their <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Google account email address.                 <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              BOARDWALKD_GOOGLE_OAUTH_CLIENT_ID and         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              BOARDWALKD_GOOGLE_OAUTH_SECRET environment    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              variables must be set. The authorized         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              redirect URI should be                        <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              https://<span style="color: #808000; text-decoration-color: #808000; font-weight: bold">&lt;hostname&gt;</span>/auth/login                 <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">[default: anonymous]                         </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--develop</span>/<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--no-develop</span>          <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">                        </span>  Runs the server in development mode with      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              auto-reloading and tracebacks                 <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">[default: no-develop]                        </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #800000; text-decoration-color: #800000">*</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--host-header-pattern</span>           <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A valid python regex pattern to match         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              accepted Host header values. This prevents    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              DNS rebinding attacks when the pattern is     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              appropriately scoped Requests reaching the    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              server that don&#x27;t match this pattern will     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              return a 404                                  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bf7f7f; text-decoration-color: #bf7f7f">[required]                                   </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--owner</span>                         <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A default admin user. Every time the server   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              starts up, this user will be enabled and      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              added to the admin role. This option must be  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              supplied when <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--auth-method</span> is anything other <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              than &#x27;anonymous&#x27;. The purpose of the owner is <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              to have an initial admin user available at    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              first start and to avoid lock-outs            <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--port</span>                          <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">INTEGER                 </span>  The non-TLS port number the server binds to.  <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--port</span> and/or <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-port</span> must be configured   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-webhook-url</span>             <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A Slack webhook URL to broadcast all key      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              events to                                     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">[env var: BOARDWALKD_SLACK_WEBHOOK_URL]      </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-error-webhook-url</span>       <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A Slack webhook URL to broadcast error events <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              to. If defined, errors will not be sent to    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              the URL defined by <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-webhook-url</span>        <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">[env var: BOARDWALKD_SLACK_ERROR_WEBHOOK_URL]</span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-app-token</span>               <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A Slack App Token for the Slack App this      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Boardwalkd instance is to connect to. If      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              specified, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-bot-token</span> must also be     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              provided.                                     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">[env var: BOARDWALKD_SLACK_APP_TOKEN]        </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-bot-token</span>               <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  A Slack OAuth Bot Token for the Slack App     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              this Boardwalkd instance is to connect to.    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">[env var: BOARDWALKD_SLACK_BOT_TOKEN]        </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--slack-slash-command-prefix</span>    <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  The prefix to use in front of Boardwalk slash <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              commands in Slack (e.g., /PREFIX-version).    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Needs to match the prefix supplied in the     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              Slack App configuration.                      <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">[env var:                                    </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bfbf7f; text-decoration-color: #bfbf7f">BOARDWALKD_SLACK_SLASH_COMMAND_PREFIX]       </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">[default: brdwlk]                            </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-crt</span>                       <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">PATH                    </span>  Path to TLS certificate chain file for use    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              along with <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-port</span>                         <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-key</span>                       <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">PATH                    </span>  Path to TLS key file for use along with       <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-port</span>                                    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-port</span>                      <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">INTEGER                 </span>  The TLS port number the server binds to. When <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              configured, the <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--url</span> option must have an     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              https:// scheme. When <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-port</span> is           <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              configured, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-crt</span> and <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--tls-key</span> must also <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              be supplied                                   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span> <span style="color: #800000; text-decoration-color: #800000">*</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--url</span>                           <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">TEXT                    </span>  The base URL where the server can be reached. <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              UI Requests that do not match the scheme or   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              host:port of this URL will automatically be   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              redirected                                    <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>                                                              <span style="color: #bf7f7f; text-decoration-color: #bf7f7f">[required]                                   </span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>    <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">--help</span>                          <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">                        </span>  Show this message and exit.                   <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">│</span>
<span style="color: #7f7f7f; text-decoration-color: #7f7f7f">╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>

</pre>
</div>
