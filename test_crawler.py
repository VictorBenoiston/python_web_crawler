import pytest
from bs4 import BeautifulSoup
from crawler_main import *

mocked_html_1st_instance = """
<body class="vsc-initialized">





































<script type="text/javascript">
    (function ($) {
        $(function () {
            var captcha = $.saj.getUrlParameter('uuidCaptcha');

            if (!captcha) {
                return;
            }

            if(!captcha){
                return;
            }
            var $processoPrinc = $('.processoPrinc');
            $processoPrinc.attr('href', $processoPrinc.attr('href') + '&uuidCaptcha=' + captcha);

            var $processoPaiApenso = $('.processoPaiApenso');
            $processoPaiApenso.attr('href', $processoPaiApenso.attr('href') + '&uuidCaptcha=' + captcha);

            $('.incidente').each(function () {
                var $incidente = $(this);
                var url = $incidente.attr('href');
                $incidente.attr('href', url + '&uuidCaptcha=' + captcha);
            });

        })
    })(jQuery);
</script>

<!-- HEADER-->
<div class="unj-entity-header">
    




<div class="unj-entity-header__actions">
    <div class="container">
        <div class="row">
            <div class="col-3 col-md-4">
                <a href="javascript:history.back();" class="unj-link-back">
                    <i id="setaVoltar" class="icon-back"></i>
                </a>
            </div>
            <div class="col-13 col-md-12 unj-ta-r">
                <!-- CDAS -->
                
                <!-- Custas -->
                
                    <button class="btn btn-secondary btn-space linkConsultaSG" onclick="location.href = 'https://www2.tjal.jus.br/ccpweb/abrirConsultaCustas.do?cdProcesso=01000O7550000&amp;nuProcesso=0710802-55.2018.8.02.0001', '_blank', 'toolbar=0,location=0,menubar=0'">
                        Visualizar custas
                    </button>
                
                <!-- Pasta digital -->
                
                    
                        
                        
                            
                        
                    
                    
                        
                        
                            <a class="linkPasta btn btn-secondary btn-space" id="linkPasta" aria-hidden="true" title="Pasta digital" href="#liberarAutoPorSenha">
                                Visualizar autos
                            </a>
                            <!-- link da pasta digital exibido somente para leitores de tela (deficientes visuais), neste caso o link anterior é ignorado pelo leitor
                            Obs: necessário manter a table devido aos atributos de acessibilidade se comportarem adequadamente com a tabela, comportamento que não é possível colocando
                            os atributos somente na tag do link-->
                            <a class="linkPasta btn btn-secondary btn-space" id="linkPastaAcessibilidade" style="font-size:0;height:0;width:0;padding:0;margin:0;border:none" href="#liberarAutoPorSenha&amp;acessibilidade=true">
                                Visualizar autos
                            </a>
                        
                    
                
                
                    
                    
                        <!-- Peticionar -->
                        
                        
                    
                
            </div>
        </div>
    </div>
</div>

    







<div class="unj-entity-header__summary">
    <div id="containerDadosPrincipaisProcesso" class="container">
        <div class="row">
            <div class="col-lg-12 col-xl-13">
                <!--principal -->
                
                    <span id="numeroProcesso" class="unj-larger-1">
                        0710802-55.2018.8.02.0001
                    </span>
                    
                    
                        <span id="labelSituacaoProcesso" class="unj-tag">Julgado Transitado</span>
                    
                    
                    
                
                <!-- incidente -->
                
                
                
            </div>

        </div>
        <div class="row">
            
                <div class="col-lg-3 col-xl-3 mb-3">
                    <span id="labelClasseProcesso" class="unj-label">Classe</span>
                    <div class="lh-1-1 line-clamp__2"><span id="classeProcesso" title="Procedimento Comum Cível">Procedimento Comum Cível</span></div>
                </div>
            
            
                <div class="col-lg-2 col-xl-3 mb-3">
                    <span id="labelAssuntoProcesso" class="unj-label">
                        Assunto
                    </span>
                    <div class="lh-1-1 line-clamp__2"> <span id="assuntoProcesso" title="Dano Material">Dano Material</span></div>
                </div>
            
            
                <div class="col-lg-2 col-xl-2 mb-2">
                    <span id="labelForoProcesso" class="unj-label">
                        Foro
                    </span>
                    <div class="lh-1-1 line-clamp__2"> <span id="foroProcesso" title="Foro de Maceió">Foro de Maceió</span></div>
                </div>
            
            
                <div class="col-lg-3 col-xl-2 mb-2">
                    <span id="labelVaraProcesso" class="unj-label">
                        Vara
                    </span>
                    <div class="lh-1-1 line-clamp__2"><span id="varaProcesso" title="4ª Vara Cível da Capital">4ª Vara Cível da Capital</span></div>
                </div>
            

            
                <div class="col-lg-3 mb-2">
                    <span id="labelJuizProcesso" class="unj-label">Juiz</span>
                    <div class="line-clamp__2"> <span id="juizProcesso" title="José Cícero Alves da Silva">José Cícero Alves da Silva</span> </div>
                </div>
            

            <!-- Processo principal -->
            

            
        </div>
    </div>
</div>

    




<div class="unj-entity-header__details">
    <div class="container">
        <div class="unj-ta-r">
            
                <a href="#maisDetalhes" class="unj-link-collapse" data-toggle="collapse" aria-expanded="true" aria-controls="maisDetalhes">
                    <span class="unj-link-collapse__show">
                        <i id="botaoExpandirDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
                        Mais
                    </span>
                    <span class="unj-link-collapse__hide">
                        <i id="botaoRecolherDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-up"></i>
                        Recolher
                    </span>
                </a>
            
        </div>
        <div id="maisDetalhes" class="collapse show" aria-expanded="false" style="">
            <div class="row unj-row--border-top">
                
                    <div class="col-lg-3 mb-2">
                        <span id="labelDistribuicaoProcesso" class="unj-label">Distribuição </span>
                        <div id="dataHoraDistribuicaoProcesso">02/05/2018 às 19:01 - Sorteio</div>
                    </div>
                
                
                
                    <div class="col-lg-3 mb-2">
                        <span id="labelControleProcesso" class="unj-label">Controle</span>
                        <div id="numeroControleProcesso">2018/000520</div>
                    </div>
                
                
                    <div class="col-lg-2 col-xl-2 mb-2">
                        <span id="labelAreaProcesso" class="unj-label">Área</span>
                        <div id="areaProcesso" class="lh-1-1 line-clamp__2"> <span title="Cível">Cível</span></div>
                    </div>
                
                
                    <div class="col-lg-2 mb-2">
                        <span id="lavelValorAcaoProcesso" class="unj-label">Valor da ação</span>
                        <div id="valorAcaoProcesso">R$         281.178,42</div>
                    </div>
                
                
                
                
                    <div class="col-lg-2 mb-2">
                        <span class="unj-label">Outros assuntos</span>
                        <div class="line-clamp__2"> <span title="Dano Moral">Dano Moral</span></div>
                    </div>
                
                
                
            </div>
        </div>
        
    </div>
</div>

</div>


<div class="div-conteudo container mb-90">
    
    
            















    
    
        




    



<aside class="aside-nav aside-nav--left">
    <div class="aside-nav__inner">
        <header class="aside-nav__main-menu__header"><span class="aside-nav__main-menu__header__text">  Menu e-SAJ</span>
            <a href="#" class="aside-nav__user__close-button close-offcanvas">
                <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--light.png" alt="">
            </a>
        </header>
        <nav class="aside-nav__main-menu">
            <ul class="aside-nav__main-menu__list" id="conteudoMenuEsaj"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Consultas</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cpopg/open.do" class="aside-nav__main-menu__list__item__link">Processos de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Ordem de Processos</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do" class="aside-nav__main-menu__list__item__link">Julgamento do 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do" class="aside-nav__main-menu__list__item__link">Publicação e Cumprimento de Atos de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cposg5/open.do" class="aside-nav__main-menu__list__item__link">Processos de 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Recolhimento de Custas</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 1º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustas.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=1&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690003" class="aside-nav__main-menu__list__item__link">Custas Iniciais de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=15&amp;flTipoCusta=5&amp;cdServicoCalculoCusta=690004" class="aside-nav__main-menu__list__item__link">Atos Avulsos de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=10&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690005" class="aside-nav__main-menu__list__item__link">Custas de Preparo de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=14&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690006" class="aside-nav__main-menu__list__item__link">Custas Juizado Especial - Recurso Inominado</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=3&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690009" class="aside-nav__main-menu__list__item__link">Custas Intermediárias de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 2º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustasSg.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdServicoCalculoCusta=690205&amp;flTipoCusta=0&amp;cdTipoCusta=1" class="aside-nav__main-menu__list__item__link">Custas iniciais de 2º Grau</a>
</li>
</ul></li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Jurisprudência</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaSimples.do" class="aside-nav__main-menu__list__item__link">Simples</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaCompleta.do" class="aside-nav__main-menu__list__item__link">Completa</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cdje" class="aside-nav__main-menu__list__item__link">Diário da Justiça Eletrônico</a>
</li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Push</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushpg" class="aside-nav__main-menu__list__item__link">1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushsg5" class="aside-nav__main-menu__list__item__link">2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Pauta de Julgamento</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pauta-julgamento/consulta" class="aside-nav__main-menu__list__item__link">Consulta da Pauta de Julgamento</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões de 1º grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirCadastro.do" class="aside-nav__main-menu__list__item__link">Pedido de Certidão de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirConferencia.do" class="aside-nav__main-menu__list__item__link">Conferência de Certidão de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirDownload.do" class="aside-nav__main-menu__list__item__link">Baixar Certidão de 1º Grau</a>
</li>
</ul></li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Conferência de Documentos</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/pg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/sg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Intimação e Citação Eletrônica</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosRecebidos.do" class="aside-nav__main-menu__list__item__link">Consulta de Recebidas</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosNaoRecebidos.do" class="aside-nav__main-menu__list__item__link">Recebimento</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 1º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoInicial.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoIntermediaria.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 2º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoInicial.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoIntermediaria.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de Turmas Recursais / Plantão (2º Grau)/ Precatórios</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoInicial.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial - TR/ Plantão TJ/ Precat.</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoIntermediaria.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário - TR/ Plantão TJ/ Precat.</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições - TR/ Plantão TJ/ Precat.</a>
</li>
</ul></li>
</ul></li></ul>
        </nav>
        <div id="esaj-beta-switcher-placeholder"></div>
    </div>
</aside>
<aside class="aside-nav aside-nav--right aside-nav__user">
    <div class="aside-nav__inner">
        <div class="aside-nav__user__sign">
            <div class="aside-nav__user__sign__brand">
                <img src="https://www2.tjal.jus.br/esaj/img/aside/brasoes/br-tjal.jpg" alt="">
            </div>
            <ul class="aside-nav__user__sign__list">
                <li><span class="aside-nav__user__sign__place">Tribunal de Justiça do Estado de Alagoas</span></li>
            </ul>
            <a href="#" class="aside-nav__user__close-button close-offcanvas">
                <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--dark.png" alt="">
            </a>
        </div>
        <hr>
        <div class="aside-nav__user__info">
            <h4 class="aside-nav__user__title">Minha conta</h4>
            <ul class="aside-nav__user__info__list">
                <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__name" id="menuNmUsuarioLogado"></span></li>
                <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__oab" id="menuUsuarioOabs">OAB: </span></li>
            </ul>
            <ul class="aside-nav__user__info__list-access">
                <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/esaj/cadastro.do">Meu perfil</a></li>
                
                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/caixapostal">Caixa Postal</a></li>
                
                <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" id="logoutLink" href="#">Sair</a></li>
            </ul>
        </div>
    </div>
</aside>
<header>
    <link rel="shortcut icon" href="https://www2.tjal.jus.br/esaj/tema/padrao/clientes/AL/imagens/favicon.ico" type="image/x-icon">
    <link href="https://www2.tjal.jus.br/esaj/app.css" rel="stylesheet" type="text/css">
    <nav class="header__navbar">
        <a class="header__navbar__menu-hamburger open__aside-nav--left navbar-menu-hamburger__item__link">
            <span class="menu-hamburger__alert" style="display:none;"></span>
            <span class="glyph glyph-hamburger"></span>
        </a>

        <h1 class="header__navbar__title" href=""><a class="linkLogo" href="https://www2.tjal.jus.br/esaj/redirecionarNovoEsaj.do"><strong>e-SAJ</strong></a> | Consulta de Processos de 1º Grau</h1>

        <ul class="header__navbar__menu header__navbar__menu--right">
            <li class="header__navbar__menu__item header__navbar__menu__item--initials">
                <a class="header__navbar__brand__initials" href="http://www.tjal.jus.br"> TJAL </a>
            </li>
            <li class="header__navbar__menu__item header__navbar__menu__item--user">
               <span class="header__navbar__name open__aside-nav--right">
                     <span id="headerNmUsuarioLogado" class="header__navbar__name__text">Identificar-se </span>
                     <span class="glyph glyph-contact header__navbar__name__icon"></span>
               </span>
            </li>
        </ul>
    </nav>
</header>
<div class="offcanvas-backdrop"></div>


<script>
    var dict = {
        'certificado.tituloCertificadoDigital': 'Certificado digital',
        'certificado.msgCarregandoCertificado': 'Carregando certificados...',
        'certificado.msgNenhumCertificadoEncontrado': 'Nenhum certificado encontrado',
        'certificado.msgErroCarregarCertificado': 'Erro ao carregar certificados',
        'certificado.msgCertificadoExpirado': '[Expirado]',
        'certificado.msgCertificadoNaoValido': '[Ainda não válido]',
        'certificado.msgCertificadoNaoIcpBrasil': '[Não ICP-Brasil]',
        'certificado.tituloProblemasAoAssinar': 'Falha de comunicação com o dispositivo de assinatura digital',

        'label.contato': 'Contato',
        'label.identificarSe': 'Identificar-se ',

        'mensagem.aguarde': 'Por favor, aguarde.',
        'mensagem.paginaNaoCarregada': 'Não foi possível carregar a página.',
        'mensagem.marcarLido': 'Marcar como lido',
        'mensagem.registrosSelecionados': 'Registros selecionados',
        'mensagem.registroJaSelecionado': 'Este registro já está selecionado',

        'mensagem.data.invalida': 'A data digitada é inválida.',
        'mensagem.data.anoInvalido': 'O ano informado deve ser maior que',
        'mensagem.data.mesInvalido': 'O mês não pode ser maior que 12.',
        'mensagem.data.mes': 'O mês',
        'mensagem.data.mesMaior29dias': 'não pode ter mais que 29 dias.',
        'mensagem.data.mesMaior28dias': 'não pode ter mais que 28 dias.',
        'mensagem.data.mesMaior31dias': 'não pode ter mais que 31 dias.',
        'mensagem.data.mesMaior30dias': 'não pode ter mais que 30 dias.',

        'mensagem.email.invalido': 'O formato do endereço de e-mail não é válido. Verifique se ele tem o formato "usuario@dominio".',
        'mensagem.email.caracteresInvalidos': 'O endereço de e-mail possui caracteres inválidos',
        'mensagem.email.usuarioInvalido': 'O formato do usuário informado no endereço de e-mail não é válido.',
        'mensagem.email.ipInvalido': 'O endereço IP informado no endereço de e-mail não é válido.',
        'mensagem.email.dominioInvalido': 'O formato do domínio informado no endereço de e-mail não é válido.',
        'mensagem.email.dominioIncompleto': 'O domínio informado no endereço de e-mail deve possuir pelo menos duas partes. Por exemplo: "usuario@empresa.com.br".',

        'mensagem.texto.tamanhoInvalido': 'O tamanho do texto digitado é maior do que o tamanho permitido. Tamanho permitido:',
        'mensagem.texto.caracter': 'O caracter',
        'mensagem.texto.caracterPosicaoInvalida': 'não está permitido na posição',

        'mensagem.numero.numeroInvalido': 'O valor digitado não é um número válido.',
        'mensagem.numero.numeroNaoPodeCasasDecimais': 'O número não pode conter casas decimais',
        'mensagem.numero.numeroCasaDecimaisInvalidas': 'O número de casas decimais é inválido. O número pode conter apenas',
        'mensagem.numero.casaDecimais': 'casas decimais',
        'mensagem.numero.numeroInteiroInvalido': 'O número de dígitos inteiros é inválido. O número pode conter apenas',
        'mensagem.numero.digitosInteiros': 'dígitos inteiros',
        'mensagem.numero.numeroTamanhoInvalido': 'O número digitado não pode ser maior que',
        'mensagem.numero.numeroZeroInvalido': 'O número digitado deve ser diferente de zero.'
    }
</script>



<script>
    var appEsajLayout = appEsajLayout || {};
    appEsajLayout.urlNovoMenuHtml = 'https://www2.tjal.jus.br/esaj/menuPortalV2Html.do?servico=190101';

    var appEsajCas = appEsajCas || {};
    appEsajCas.urlServicoConteudoIdentificacao = 'https://www2.tjal.jus.br/sajcas/conteudoIdentificacaoJson?script=1689318173416&retorno=' + encodeURIComponent(location.href);
</script>
<script src="https://www2.tjal.jus.br/esaj/js/portalV2-bundle.js?n=806192629"></script>

<script src="https://www2.tjal.jus.br/sajcas/seletorVersaoBeta.js?n=cf11148e-e81a-405e-9a9a-d6579880c0c7&amp;versao=2"></script>

    




            
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
            
                
                    
                        














                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
            
                
                    
                    
                        




























<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle tituloDoBloco">Partes do processo</h2>
        
    
</div>

<!--  cabecalho da tabela de lista (partes) -->


<!--  dados da lista partes principais (partes) -->
<table id="tablePartesPrincipais" style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
    
        









<tbody><tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    José Carlos Cerqueira Souza Filho
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Vinicius Faria de Cerqueira
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

    
        









<tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Ré&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    Cony Engenharia Ltda.
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Carlos Henrique de Mendonça Brandão
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Guilherme Freire Furtado
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogada:&nbsp;</span>
                
                    
                    
                        Maria Eugênia Barreiros de Mello
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Vítor Reis de Araujo Carvalho
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

    
</tbody></table>



    <!--  dados da lista todas as partes (partes) -->
    <table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0">
        
            









<tbody><tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    José Carlos Cerqueira Souza Filho
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Vinicius Faria de Cerqueira
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

        
            









<tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Autora&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    Livia Nascimento da Rocha
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Vinicius Faria de Cerqueira
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

        
            









<tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Ré&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    Cony Engenharia Ltda.
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Carlos Henrique de Mendonça Brandão
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Guilherme Freire Furtado
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogada:&nbsp;</span>
                
                    
                    
                        Maria Eugênia Barreiros de Mello
                    
                &nbsp;
                
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Vítor Reis de Araujo Carvalho
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

        
            









<tr class="fundoClaro">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
        <span class="mensagemExibindo tipoDeParticipacao">Réu&nbsp;</span>
    </td>
    <td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">
        
            
                
                
                    Banco do Brasil S A
                
            

            
         
        
            
                <br>
                <span class="mensagemExibindo">Advogado:&nbsp;</span>
                
                    
                    
                        Nelson Wilians Fratoni Rodrigues
                    
                &nbsp;
                
            
        
        
    </td>
</tr>

        
    </tbody></table>
    <div id="divLinksTituloBlocoPartes" style="text-align:right">
        









<input id="mensagemNaoExibidapartes" type="hidden" value="">

    <input id="linkNaoExibidopartes" type="hidden" value="<span id=&quot;setasDireitapartes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

<span id="mensagensExibindopartes" class="mensagemExibindo">

</span> &nbsp;

    <a id="linkpartes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
        <span id="setasDireitapartes" class="setasDireita">
            <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
        </span>
        Mais
    </a>

<script>
    $(function() {
        var controlarLink = function() {
            var $linkNaoExibido = $('input#linkNaoExibidopartes');
            var conteudoLinkNaoApresentado = $linkNaoExibido.val();
            var $link = $('a#linkpartes');
            
            $linkNaoExibido.val($link.html());
            $link.html(conteudoLinkNaoApresentado);
        };

        var controlarMensagem = function() {
            var $mensagemNaoExibida = $('input#mensagemNaoExibidapartes');
            var $spanMensagem = $('span#mensagensExibindopartes');
            var mensagemExibida = $spanMensagem.html();
            var mensagemNaoExibida = $mensagemNaoExibida.val();
            
            $spanMensagem.html(mensagemNaoExibida);
            $mensagemNaoExibida.val(mensagemExibida);
        };

        var controlarMensagemLink = function() {
            controlarMensagem();
            controlarLink();
        };
        
        var esconderElementosExtrasMostrarDefault = function() {
            $('#tableTodasPartes').hide();
            $('#tablePartesPrincipais').show();
        };

        var mostrarElementosExtrasEsconderDefault = function() {
            $('#tablePartesPrincipais').hide();
            $('#tableTodasPartes').show();
        };

        var initPagina = function() {
            var setasDireita = '<span id="setasDireitapartes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
            var $linkEscondido = $('input#linkNaoExibidopartes');
            $linkEscondido.val(setasDireita+$linkEscondido.val());
        };

        var bindLink = function() {
            var $link = $('a#linkpartes');
            $link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
            $link.bind('click', controlarMensagemLink);
        };

        initPagina();
        bindLink();
        esconderElementosExtrasMostrarDefault();
    });
</script>

    </div>


                    
                    
                    
                    
                    
                    
                    
                    
                    
                
            
                
                    
                    
                    
                    
                    
                        


  























<div style="padding-top: 10px;">
    
    
        
        
        
        
    

    
        
        
            <h2 class="subtitle tituloDoBloco">Movimentações</h2>
        
    
</div>


 
    

<table style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
    
        
            <thead>
                <tr>
                  <th width="120" class="label" style="vertical-align: bottom">Data</th>
                  <th valign="middle" width="20" aria-hidden="true">&nbsp;</th>
                  <th valign="middle" class="label">Movimento</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </thead>

            
            <tbody id="tabelaUltimasMovimentacoes">
                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Execução de Sentença Iniciada
                
            
            
            <br>
            <span style="font-style: italic;">
                Seq.: 01 - Cumprimento de sentença
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0282/2023
Data da Publicação: 08/05/2023
Número do Diário: 3296
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0282/2023
Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)
Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Recebido pela Contadoria UNIFICADA
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato Ordinatório - Artigo 162, §4º, CPC
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Ato Ordinatório- Remessa à contadoria
            </span>
            
        </td>
    </tr>
    


                
            </tbody>
            
            
            <tbody style="display: none;" id="tabelaTodasMovimentacoes">
                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Execução de Sentença Iniciada
                
            
            
            <br>
            <span style="font-style: italic;">
                Seq.: 01 - Cumprimento de sentença
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0282/2023
Data da Publicação: 08/05/2023
Número do Diário: 3296
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0282/2023
Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)
Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Recebido pela Contadoria UNIFICADA
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato Ordinatório - Artigo 162, §4º, CPC
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Ato Ordinatório- Remessa à contadoria
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-48258006" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-48258006" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)<br><b>Vencimento: </b>25/05/2023
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            03/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Transitado em Julgado
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            03/05/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Recebimento da Instância Superior -  Altera situação para "Julgado"
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            26/04/2023
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Recebido recurso eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Data do julgamento: 07/10/2021
Trânsito em julgado: 
Tipo de julgamento: Acórdão
Decisão: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. 
Situação do provimento: 
Relator: Des. Otávio Leão Praxedes
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            22/02/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            10/02/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.21.70031538-2
Tipo da Petição: Contrarrazões
Data: 10/02/2021 19:27

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0003/2021
Data da Publicação: 21/01/2021
Número do Diário: 2738
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0003/2021
Teor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário
Advogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            04/01/2021
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-36544373" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-36544373" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato Ordinatório - Artigo 162, §4º, CPC
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            18/12/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.20.70269584-0
Tipo da Petição: Juntada de Instrumento de Procuração
Data: 18/12/2020 17:23

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            18/12/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.20.70269581-5
Tipo da Petição: Recurso de Apelação
Data: 18/12/2020 17:18

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            15/12/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.20.70265228-8
Tipo da Petição: Recurso de Apelação
Data: 15/12/2020 13:26

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0912/2020
Data da Publicação: 25/11/2020
Número do Diário: 2711
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0912/2020
Data da Publicação: 25/11/2020
Número do Diário: 2711
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0912/2020
Data da Publicação: 25/11/2020
Número do Diário: 2711
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0912/2020
Data da Publicação: 25/11/2020
Número do Diário: 2711
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            23/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0912/2020
Teor do ato: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.
Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
        
    
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            23/11/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-36008611" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=36008611&amp;nmRecursoAcessado=Julgado+procedente+em+parte+do+pedido" target="_blank">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-36008611" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=36008611&amp;nmRecursoAcessado=Julgado+procedente+em+parte+do+pedido" target="_blank"> Julgado procedente em parte do pedido
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.<br><b>Vencimento: </b>16/12/2020
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            23/09/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Conclusos
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
        
    
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            16/08/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-34722317" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=34722317&amp;nmRecursoAcessado=Visto+em+Autoinspe%C3%A7%C3%A3o" target="_blank">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-34722317" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=34722317&amp;nmRecursoAcessado=Visto+em+Autoinspe%C3%A7%C3%A3o" target="_blank"> Visto em Autoinspeção
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Despacho Visto em Autoinspeção
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2020
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.20.70092549-0
Tipo da Petição: Pedido de Andamento do proc./sent./decisões/desp.
Data: 11/05/2020 13:28

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            10/12/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Conclusos
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
        
    
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/11/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-31112627" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=31112627&amp;nmRecursoAcessado=Despacho+de+Mero+Expediente" target="_blank">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-31112627" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=31112627&amp;nmRecursoAcessado=Despacho+de+Mero+Expediente" target="_blank"> Despacho de Mero Expediente
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                DESPACHO Compulsando detidamente o feito, verifico que este inclui-se nos processos com prioridade de impulsionamento, consoante recomendação exarada pelo Conselho Nacional de Justiça, a qual determina a priorização de andamento das demandas paralisadas há mais de 100 (dias). Destarte, considerando que cada uma desses processos exige análise acurada por este magistrado a fim de que lhe seja dado efetivo provimento, determino a conclusão de todos os autos que se amoldem à hipótese alhures delineada - de competência do gabinete - para análise e devido impulsionamento, este especificamente, na fila concluso - impulso ao feito. Cumpra-se. Maceió(AL), 11 de novembro de 2019. José Cícero Alves da Silva Juiz de Direito
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            12/07/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.19.70150828-9
Tipo da Petição: Petição
Data: 11/07/2019 23:50

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            12/02/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.19.70034823-7
Tipo da Petição: Petição
Data: 12/02/2019 14:58

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/02/2019
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.19.70032532-6
Tipo da Petição: Petição
Data: 11/02/2019 09:13

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/12/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Conclusos
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            05/12/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70259903-1
Tipo da Petição: Petição
Data: 05/12/2018 16:46

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            29/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70255192-6
Tipo da Petição: Petição
Data: 29/11/2018 15:07

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            28/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0499/2018
Data da Publicação: 29/11/2018
Número do Diário: 2233
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            27/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0499/2018
Teor do ato: ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018
Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Rafael Sganzerla Durand (OAB 10132A/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            27/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-26689702" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-26689702" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            26/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70251514-8
Tipo da Petição: Impugnação à Contestação
Data: 26/11/2018 15:37

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            26/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70251511-3
Tipo da Petição: Impugnação à Contestação
Data: 26/11/2018 15:35

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            09/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0456/2018
Data da Publicação: 12/11/2018
Número do Diário: 2222
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            08/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0456/2018
Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário
Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/11/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-26414651" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-26414651" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário<br><b>Vencimento: </b>29/11/2018
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            16/10/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documentos
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70221617-5
Tipo da Petição: Contestação
Data: 16/10/2018 14:43

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            10/10/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documentos
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70218154-1
Tipo da Petição: Contestação
Data: 10/10/2018 14:04

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Documento
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-25822019" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-25822019" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Audiência Realizada
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                Assentada - Genérico
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            24/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70203989-3
Tipo da Petição: Petição
Data: 24/09/2018 10:09

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            21/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70203544-8
Tipo da Petição: Petição
Data: 21/09/2018 18:07

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            21/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70203528-6
Tipo da Petição: Petição
Data: 21/09/2018 17:42

            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            21/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de Petição
                
            
            
            <br>
            <span style="font-style: italic;">
                Nº Protocolo: WMAC.18.70203260-0
Tipo da Petição: Petição
Data: 21/09/2018 13:58

            </span>
            
        </td>
    </tr>
    


                
                    










    
        
    
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            20/09/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-25787004" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=25787004&amp;nmRecursoAcessado=Visto+em+correi%C3%A7%C3%A3o" target="_blank">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-25787004" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=25787004&amp;nmRecursoAcessado=Visto+em+correi%C3%A7%C3%A3o" target="_blank"> Visto em correição
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                DESPACHO VISTO EM CORREIÇÃO
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/06/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de AR - Cumprido
                
            
            
            <br>
            <span style="font-style: italic;">
                Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário: 
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            06/06/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Juntada de AR - Cumprido
                
            
            
            <br>
            <span style="font-style: italic;">
                Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969745TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0001, emitido para Banco do Brasil S A. Usuário: 
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            15/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0220/2018
Data da Publicação: 16/05/2018
Número do Diário: 2105
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            15/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Ato Publicado
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação :0220/2018
Data da Publicação: 16/05/2018
Número do Diário: 2105
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0220/2018
Teor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.&nbsp;Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.&nbsp;No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.&nbsp;Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito
Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Disponibilização no Diário da Justiça Eletrônico
                
            
            
            <br>
            <span style="font-style: italic;">
                Relação: 0220/2018
Teor do ato: Conciliação
Data: 24/09/2018 Hora 14:00
Local: Sala de Audiência
Situacão: Pendente
Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-24228218" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-24228218" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Carta Expedida
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-24228179" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-24228179" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Carta Expedida
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            11/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Audiência Designada
                
            
            
            <br>
            <span style="font-style: italic;">
                Conciliação
Data: 24/09/2018 Hora 14:00
Local: Sala de Audiência
Situacão: Realizada
            </span>
            
        </td>
    </tr>
    


                
                    










    
        
    
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            10/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
                
                    
                    
                        
                    
                

                <a class="linkMovVincProc" id="linkMovVincProc-24187801" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=24187801&amp;nmRecursoAcessado=N%C3%A3o+Concedida+a+Antecipa%C3%A7%C3%A3o+de+tutela" target="_blank">
                    <img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
                </a>
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                    <a class="linkMovVincProc" id="linkMovVincProc-2-24187801" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=24187801&amp;nmRecursoAcessado=N%C3%A3o+Concedida+a+Antecipa%C3%A7%C3%A3o+de+tutela" target="_blank"> Não Concedida a Antecipação de tutela
                    </a>
                
                
            
            
            <br>
            <span style="font-style: italic;">
                DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.&nbsp;Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.&nbsp;No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.&nbsp;Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito<br><b>Vencimento: </b>01/06/2018
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            03/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Conclusos
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoClaro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            02/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Conclusos
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
                    










    
    
        
    



    <tr class="fundoEscuro containerMovimentacao" style="">
        <td class="dataMovimentacao" width="120" style="vertical-align: top">
            02/05/2018
        </td>
        <td width="20" valign="top" aria-hidden="true">
            
        </td>
        <td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">
            
            
                
                
                    Distribuído por Sorteio
                
            
            
            <br>
            <span style="font-style: italic;">
                
            </span>
            
        </td>
    </tr>
    


                
            </tbody>

        
        
    
</table>

    <div id="divLinksTituloBlocoMovimentacoes" style="text-align:right">
        









<input id="mensagemNaoExibidamovimentacoes" type="hidden" value="">

    <input id="linkNaoExibidomovimentacoes" type="hidden" value="<span id=&quot;setasDireitamovimentacoes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

<span id="mensagensExibindomovimentacoes" class="mensagemExibindo">

</span> &nbsp;

    <a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
        <span id="setasDireitamovimentacoes" class="setasDireita">
            <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
        </span>
        Mais
    </a>

<script>
    $(function() {
        var controlarLink = function() {
            var $linkNaoExibido = $('input#linkNaoExibidomovimentacoes');
            var conteudoLinkNaoApresentado = $linkNaoExibido.val();
            var $link = $('a#linkmovimentacoes');
            
            $linkNaoExibido.val($link.html());
            $link.html(conteudoLinkNaoApresentado);
        };

        var controlarMensagem = function() {
            var $mensagemNaoExibida = $('input#mensagemNaoExibidamovimentacoes');
            var $spanMensagem = $('span#mensagensExibindomovimentacoes');
            var mensagemExibida = $spanMensagem.html();
            var mensagemNaoExibida = $mensagemNaoExibida.val();
            
            $spanMensagem.html(mensagemNaoExibida);
            $mensagemNaoExibida.val(mensagemExibida);
        };

        var controlarMensagemLink = function() {
            controlarMensagem();
            controlarLink();
        };
        
        var esconderElementosExtrasMostrarDefault = function() {
            $('#tabelaTodasMovimentacoes').hide();
            $('#tabelaUltimasMovimentacoes').show();
        };

        var mostrarElementosExtrasEsconderDefault = function() {
            $('#tabelaUltimasMovimentacoes').hide();
            $('#tabelaTodasMovimentacoes').show();
        };

        var initPagina = function() {
            var setasDireita = '<span id="setasDireitamovimentacoes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
            var $linkEscondido = $('input#linkNaoExibidomovimentacoes');
            $linkEscondido.val(setasDireita+$linkEscondido.val());
        };

        var bindLink = function() {
            var $link = $('a#linkmovimentacoes');
            $link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
            $link.bind('click', controlarMensagemLink);
        };

        initPagina();
        bindLink();
        esconderElementosExtrasMostrarDefault();
    });
</script>

    </div>

        

    

                    
                    
                    
                    
                    
                    
                
            
                
                    
                    
                    
                    
                        




















<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle tituloDoBloco">Petições diversas</h2>
        
    
</div>

<!-- Tabela de petições diversas -->
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    
        
            <thead>
                <tr class="label">
                  <th width="140" style="text-align:left">Data</th>
                  <th width="*">Tipo</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td></td>
                    <td></td>
                </tr>
            </thead>
            <tbody>
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                21/09/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                21/09/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                21/09/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                24/09/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                10/10/2018
                            </td>
                            <td width="*">
                                Contestação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                16/10/2018
                            </td>
                            <td width="*">
                                Contestação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                26/11/2018
                            </td>
                            <td width="*">
                                Impugnação à Contestação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                26/11/2018
                            </td>
                            <td width="*">
                                Impugnação à Contestação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                29/11/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                05/12/2018
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                11/02/2019
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                12/02/2019
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                11/07/2019
                            </td>
                            <td width="*">
                                Petição <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                11/05/2020
                            </td>
                            <td width="*">
                                Pedido de Andamento do proc./sent./decisões/desp. <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                15/12/2020
                            </td>
                            <td width="*">
                                Recurso de Apelação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                18/12/2020
                            </td>
                            <td width="*">
                                Recurso de Apelação <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoClaro"> 
                            <td width="140" style="text-align:left">
                                18/12/2020
                            </td>
                            <td width="*">
                                Juntada de Instrumento de Procuração <br>
                                
                            </td>
                        </tr>
                    
                
                    
                        <tr class="fundoEscuro"> 
                            <td width="140" style="text-align:left">
                                10/02/2021
                            </td>
                            <td width="*">
                                Contrarrazões <br>
                                
                            </td>
                        </tr>
                    
                
            </tbody>
        
        
    
</table>
<!--  Tabela de petições diversas -->


                    
                    
                    
                    
                    
                    
                    
                
            
                
                    
                    
                    
                        












<script type="text/javascript">
    (function($) {
        $(function(){
            var captcha = $.saj.getUrlParameter('uuidCaptcha');
            if(!captcha){
                return;
            }
            $('.incidente a').each(function(){
                var $incidente = $(this);
                var url = $incidente.attr('href');
                $incidente.attr('href', url+'&uuidCaptcha='+captcha);
            });
        })
    })(jQuery);
</script>











<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle tituloDoBloco">Incidentes, ações incidentais, recursos e execuções de sentenças</h2>
        
    
</div>

<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">

    
        <tbody><tr class="label">
            <th width="140">
                Recebido em
            </th>
            <th width="*" class="label">
                Classe
            </th>
        </tr>
        <tr class="fundoEscuro" height="2" aria-hidden="true">
            <td></td><td></td>
        </tr>

        
            
            <tr class="fundoClaro">
              <td width="140" style="text-align:left">
                05/05/2023
              </td>
            <td width="*">
                
                    
                        <a class="incidente" href="/cpopg/show.do?localPesquisa.cdLocal=1&amp;processo.codigo=01000O7550001&amp;processo.foro=1" target="_top">
                            Cumprimento de sentença
                            
                                 - 00001
                            
                            
                        </a>
                    
                    
                
            </td>
        </tr>        
    
    
    

</tbody></table>
<!--  Incidentes -->

                    
                    
                    
                    
                    
                    
                    
                    
                
            
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                        














<script type="text/javascript">
    (function ($) {
        $(function () {
            var captcha = $.saj.getUrlParameter('uuidCaptcha');

            if(!captcha){
                return;
            }
            $.each($('.processoApensado'), function (i, value) {
                var $link = $(value);
                $link.attr('href', $link.attr('href') + '&uuidCaptcha=' + captcha);
            })

        })
    })(jQuery);
</script>









<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle tituloDoBloco">Apensos, Entranhados e Unificados</h2>
        
    
</div>



    
        <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
            <tbody id="dadosApensosNaoDisponiveis">
            <tr>
                <td colspan="3" align="left">Não há processos apensados, entranhados e unificados a este processo.</td>
            </tr>
            </tbody>
        </table>

    
    


                    
                
            
                
                    
                    
                    
                    
                    
                    
                        







<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle tituloDoBloco">Audiências</h2>
        
    
</div>

                        












    
        
            
                
            
            
        
    
    

<a name="audienciasPlaceHolder"></a>
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    
        
            <tbody><tr class="label">
                <th align="left" valign="top" width="140">Data</th>
                <th align="left" valign="top" width="*">Audiência</th>
                <th align="left" valign="top" width="100">Situação</th>
                <th align="left" valign="top" width="100">Qt. Pessoas</th>
            </tr>
            <tr class="fundoEscuro" height="2" aria-hidden="true">
                <td colspan="4"></td>
            </tr>
            
                <tr class="fundoClaro">
                    <td valign="top" align="left" width="140">
                        24/09/2018
                    </td>
                    
                        
                        
                            <td valign="top" align="left" width="*">
                                Conciliação
                            </td>
                        
                    

                    <td align="left" valign="top" width="100">
                        Realizada
                    </td>
                    <td align="left" valign="top" width="100">
                        7
                    </td>
                </tr>
            
        
        
    
</tbody></table>

                    
                    
                    
                    
                    
                
            
                
                    
                    
                    
                    
                    
                    
                    
                        














<form id="popupCdas" style="display: none;">
    <!--  dados da lista (CDAs) -->
    <div style="height:210px; overflow: auto;">
        <table id="tableCdasPrincipais" style="margin-left:10px; margin-top:1px; width: 98%;">
            <thead>
                <tr class="fundoClaro">
                    <th style="text-align:left;">Número CDA</th>
                    <th style="text-align:left;">Valor</th>
                    <th style="text-align:left;">Dt. CDA</th>
                    <th style="text-align:left;">Valor atualizado</th>
                    <th style="text-align:left;">Dt. atualização</th>
                    <th style="text-align:left;">Situação</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td colspan="6">
                </td></tr>
            </thead>
            <tbody>
                
            </tbody>
        </table>
    </div>
</form>

                    
                    
                    
                    
                
            
    

    












    <form action="/cpopg/show.do?processo.codigo=01000O7550000&amp;processo.foro=1&amp;processo.numero=0710802-55.2018.8.02.0001" id="popupSenha" style="display: none;" method="POST">
        
        <table role="document">
            <tbody><tr>
                <td colspan="2" style="padding-bottom:20px">Atendendo a resolução 121 do CNJ.</td>
            </tr>
            
                <tr>
                    <td colspan="2" style="padding-bottom:20px">Se for advogado(a) nesse processo, é necessário<span id="identificacao"><strong><a href="https://www2.tjal.jus.br/esaj/identificacao.do?retorno=https%3A//www2.tjal.jus.br/cpopg/show.do%3Fprocesso.codigo%3D01000O7550000%26processo.foro%3D1%26processo.numero%3D0710802-55.2018.8.02.0001">Identificar-se</a></strong></span></td>
                    
                        
                        
                            <script language="javascript" type="text/JavaScript" src="https://www2.tjal.jus.br/sajcas/conteudoIdentificacao?script=1689369850984"></script>
                        
                    
                </tr>
            
            <tr align="center">
                <td align="left" colspan="2" style="padding-bottom:20px">
                    <div style="float:left; line-height:30px;">Se for uma parte ou interessado, digite a senha do processo</div>
                    <div style="float:left;width: 140px; padding-left:15px">
                        <input type="password" name="senhaProcesso" maxlength="12" value="" rotulo="" class="form-control" id="senhaProcesso">
                        <input type="hidden" name="idRecursoQueProvocouLiberacaoPorSenha" value="">
                    </div>
                    <div class="unj-form-control-group__icon">
                        <div class="dropdown show">
                            <a href="javascript:;" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <span class="glyph glyph-info" aria-hidden="true"></span>
                            </a>
                            <div class="dropdown-menu tooltip-campos" aria-labelledby="dropdownMenuLink">
                                
                                    É necessário informar uma senha para acessar processo em segredo de justiça, bem como para acessar autos dos demais processos.<br><br>
                                    Se for parte do processo e ainda não possua uma senha, <b>solicite-a no cartório</b>.<br><br>
                                
                                
                            </div>
                        </div>
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    

















    
    
        
    <input type="button" name="btFechar" value="Cancelar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotao " id="botaoFecharPopupSenha">


                    
                        
                        
                            













    
        
    
    <input type="submit" name="btEnviarSenha" value="Continuar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotaoDefault btn-space" id="btEnviarSenha">


                        
                    
                </td>
            </tr>
        </tbody></table>
    </form>




    
</div>
















    
    
        



<footer>
    <nav class="navbar__footer">
        <div class="navbar__footer__container">

            <ul class="navbar__footer__list-brand">
                <li class="navbar__footer__list-brand__item">
                    <a href="https://www.softplan.com.br/solucoes/saj-tribunais/" class="navbar__footer__list-brand__item__link link_softplan_tribunais">
                        <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-saj.png" alt="SAJ">
                    </a>
                </li>
                <li class="navbar__footer__list-brand__item">
                    <a href="https://www.softplan.com.br/" class="navbar__footer__list-brand__item__link link_softplan">
                        <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-softplan.png" alt="Softplan">
                    </a>
                </li>
            </ul>

            <ul class="navbar__footer__list-actions">
            </ul>
        </div>
    </nav>
</footer>

    





<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":204,"applicationID":"111652883","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfTxZHQRZCFkpRAkNZXw9LYFsMQSQHRAhYXg==","queueTime":0}</script>

<article style="z-index: 2147483647;"></article></body>
"""

mocked_html_2nd_instance = """
<body class="vsc-initialized"><input type="hidden" name="cdProcesso" value="P00006BXP0000">
    
    




<!-- HEADER-->
<div class="unj-entity-header">

    




<div class="unj-entity-header__actions">
    <div class="container">
        <div class="row">
            <div class="col-3 col-md-4">
                <a href="javascript:history.back();" class="unj-link-back">
                    <i class="icon-back"></i>
                </a>
            </div>
            <div class="col-13 col-md-12 unj-ta-r">
                <!-- Pasta digital -->
                
                    
                    <a class="linkPasta btn btn-secondary btn-space" id="pbVisualizarAutos" title="Pasta Digital" href="#" name="">
                        Visualizar autos
                    </a>
                
                <!-- Peticionar -->
                
            </div>
        </div>
    </div>
</div>

    






<div class="unj-entity-header__summary">
    <div class="container">
        <div class="row">
            <div class="col-md-13">
                <!--principal -->
                
                    <span class="unj-larger-1 " id="numeroProcesso">
                        0710802-55.2018.8.02.0001
                    </span>
                    
                    
                        <span class="unj-tag" id="situacaoProcesso">Baixado</span>
                    
                    
                    
                
                <!-- incidente -->
                
                
            </div>
        </div>
        <div class="row">
            
                <div class="col-md-3">
                    <span class="unj-label">Classe</span>
                    <div class="lh-1-1 line-clamp__2" id="classeProcesso"> <span title="Apelação Cível">Apelação Cível</span></div>
                </div>
            
            
                <div class="col-md-4">
                    <span class="unj-label">
                        Assunto
                    </span>
                    <div class="lh-1-1 line-clamp__2" id="assuntoProcesso"><span title="Obrigações">Obrigações</span></div>
                </div>
            
            
                <div class="col-md-3">
                    <span class="unj-label">Seção</span>
                    <div class="lh-1-1 line-clamp__2" id="secaoProcesso"> <span title="Tribunal de Justiça">Tribunal de Justiça</span></div>
                </div>
            
            
                <div class="col-md-3">
                    <span class="unj-label">Órgão Julgador</span>
                    <div class="lh-1-1 line-clamp__2" id="orgaoJulgadorProcesso"> <span title="Vice-Presidência">Vice-Presidência</span></div>
                </div>
            
            
                <div class="col-md-2">
                    <span class="unj-label">Área</span>
                    <div class="lh-1-1 line-clamp__2" id="areaProcesso"><span title="Cível">Cível</span></div>
                </div>
            
            <!-- Processo principal -->
            
        </div>
    </div>
</div>

    





<div class="unj-entity-header__details">
    <div class="container">
        <div class="unj-ta-r">
            <a href="#maisDetalhes" class="unj-link-collapse" data-toggle="collapse" aria-expanded="true" aria-controls="maisDetalhes">
                <span class="unj-link-collapse__show">
                    <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
                    Mais
                </span>
                <span class="unj-link-collapse__hide">
                    <i class="unj-link-collapse__icon glyph glyph-chevron-up"></i>
                    Recolher
                </span>
            </a>
        </div>
        <div id="maisDetalhes" class="collapse show" aria-expanded="false" style="">
            <div class="row unj-row--border-top">
                
                
                
                
                    <div class="col-lg-3 mb-2">
                        <span class="unj-label">Relator</span>
                        <div class="line-clamp__2" id="relatorProcesso"><span title="VICE PRESIDENTE DO TRIBUNAL DE JUSTIÇA DE ALAGOAS">VICE PRESIDENTE DO TRIBUNAL DE JUSTIÇA DE ALAGOAS</span></div>
                    </div>
                
                
                
                    <div class="col-lg-3 mb-2">
                        <span class="unj-label">Valor da ação</span>
                        <div class="line-clamp__2" id="valorAcaoProcesso"><span title="281.178,42">281.178,42</span></div>
                    </div>
                
                
                
                
                
                
                    <div class="col-lg-3 mb-2">
                        <span class="unj-label">Origem</span>
                        <div class="line-clamp__2"><span title="Comarca de Maceió / Foro de Maceió / 4ª Vara Cível da Capital">Comarca de Maceió / Foro de Maceió / 4ª Vara Cível da Capital</span></div>
                    </div>
                
                
                    <div class="col-lg-3 mb-2">
                        <span class="unj-label">Volume / Apenso</span>
                        <div class="line-clamp__2" id="volumeApensoProcesso"><span title="1 / 0">1 / 0</span></div>
                    </div>
                
                
                
                
                

            </div>
        </div>
    </div>
</div>

</div>


  
  <div class="div-conteudo container unj-mb-40">
    















    
    
        




    



<aside class="aside-nav aside-nav--left">
    <div class="aside-nav__inner">
        <header class="aside-nav__main-menu__header"><span class="aside-nav__main-menu__header__text">  Menu e-SAJ</span>
            <a href="#" class="aside-nav__user__close-button close-offcanvas">
                <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--light.png" alt="">
            </a>
        </header>
        <nav class="aside-nav__main-menu">
            <ul class="aside-nav__main-menu__list" id="conteudoMenuEsaj"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Consultas</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cpopg/open.do" class="aside-nav__main-menu__list__item__link">Processos de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Ordem de Processos</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do" class="aside-nav__main-menu__list__item__link">Julgamento do 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do" class="aside-nav__main-menu__list__item__link">Publicação e Cumprimento de Atos de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cposg5/open.do" class="aside-nav__main-menu__list__item__link">Processos de 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Recolhimento de Custas</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 1º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustas.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=1&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690003" class="aside-nav__main-menu__list__item__link">Custas Iniciais de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=15&amp;flTipoCusta=5&amp;cdServicoCalculoCusta=690004" class="aside-nav__main-menu__list__item__link">Atos Avulsos de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=10&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690005" class="aside-nav__main-menu__list__item__link">Custas de Preparo de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=14&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690006" class="aside-nav__main-menu__list__item__link">Custas Juizado Especial - Recurso Inominado</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=3&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690009" class="aside-nav__main-menu__list__item__link">Custas Intermediárias de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 2º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustasSg.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdServicoCalculoCusta=690205&amp;flTipoCusta=0&amp;cdTipoCusta=1" class="aside-nav__main-menu__list__item__link">Custas iniciais de 2º Grau</a>
</li>
</ul></li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Jurisprudência</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaSimples.do" class="aside-nav__main-menu__list__item__link">Simples</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaCompleta.do" class="aside-nav__main-menu__list__item__link">Completa</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cdje" class="aside-nav__main-menu__list__item__link">Diário da Justiça Eletrônico</a>
</li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Push</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushpg" class="aside-nav__main-menu__list__item__link">1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushsg5" class="aside-nav__main-menu__list__item__link">2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Pauta de Julgamento</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pauta-julgamento/consulta" class="aside-nav__main-menu__list__item__link">Consulta da Pauta de Julgamento</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões de 1º grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirCadastro.do" class="aside-nav__main-menu__list__item__link">Pedido de Certidão de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirConferencia.do" class="aside-nav__main-menu__list__item__link">Conferência de Certidão de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirDownload.do" class="aside-nav__main-menu__list__item__link">Baixar Certidão de 1º Grau</a>
</li>
</ul></li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Conferência de Documentos</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/pg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/sg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Intimação e Citação Eletrônica</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosRecebidos.do" class="aside-nav__main-menu__list__item__link">Consulta de Recebidas</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosNaoRecebidos.do" class="aside-nav__main-menu__list__item__link">Recebimento</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 1º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoInicial.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoIntermediaria.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 1º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 1º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 2º Grau</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoInicial.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoIntermediaria.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 2º Grau</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 2º Grau</a>
</li>
</ul></li>
<li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de Turmas Recursais / Plantão (2º Grau)/ Precatórios</a>
<ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoInicial.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial - TR/ Plantão TJ/ Precat.</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoIntermediaria.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário - TR/ Plantão TJ/ Precat.</a>
</li>
<li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições - TR/ Plantão TJ/ Precat.</a>
</li>
</ul></li>
</ul></li></ul>
        </nav>
        <div id="esaj-beta-switcher-placeholder"></div>
    </div>
</aside>
<aside class="aside-nav aside-nav--right aside-nav__user">
    <div class="aside-nav__inner">
        <div class="aside-nav__user__sign">
            <div class="aside-nav__user__sign__brand">
                <img src="https://www2.tjal.jus.br/esaj/img/aside/brasoes/br-tjal.jpg" alt="">
            </div>
            <ul class="aside-nav__user__sign__list">
                <li><span class="aside-nav__user__sign__place">Tribunal de Justiça do Estado de Alagoas</span></li>
            </ul>
            <a href="#" class="aside-nav__user__close-button close-offcanvas">
                <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--dark.png" alt="">
            </a>
        </div>
        <hr>
        <div class="aside-nav__user__info">
            <h4 class="aside-nav__user__title">Minha conta</h4>
            <ul class="aside-nav__user__info__list">
                <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__name" id="menuNmUsuarioLogado"></span></li>
                <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__oab" id="menuUsuarioOabs">OAB: </span></li>
            </ul>
            <ul class="aside-nav__user__info__list-access">
                <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/esaj/cadastro.do">Meu perfil</a></li>
                
                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/caixapostal">Caixa Postal</a></li>
                
                <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" id="logoutLink" href="#">Sair</a></li>
            </ul>
        </div>
    </div>
</aside>
<header>
    <link rel="shortcut icon" href="https://www2.tjal.jus.br/esaj/tema/padrao/clientes/AL/imagens/favicon.ico" type="image/x-icon">
    <link href="https://www2.tjal.jus.br/esaj/app.css" rel="stylesheet" type="text/css">
    <nav class="header__navbar">
        <a class="header__navbar__menu-hamburger open__aside-nav--left navbar-menu-hamburger__item__link">
            <span class="menu-hamburger__alert" style="display:none;"></span>
            <span class="glyph glyph-hamburger"></span>
        </a>

        <h1 class="header__navbar__title" href=""><a class="linkLogo" href="https://www2.tjal.jus.br/esaj/redirecionarNovoEsaj.do"><strong>e-SAJ</strong></a> | Consulta de Processos de 2º Grau</h1>

        <ul class="header__navbar__menu header__navbar__menu--right">
            <li class="header__navbar__menu__item header__navbar__menu__item--initials">
                <a class="header__navbar__brand__initials" href="http://www.tjal.jus.br"> TJAL </a>
            </li>
            <li class="header__navbar__menu__item header__navbar__menu__item--user">
               <span class="header__navbar__name open__aside-nav--right">
                     <span id="headerNmUsuarioLogado" class="header__navbar__name__text">Identificar-se </span>
                     <span class="glyph glyph-contact header__navbar__name__icon"></span>
               </span>
            </li>
        </ul>
    </nav>
</header>
<div class="offcanvas-backdrop"></div>


<script>
    var dict = {
        'certificado.tituloCertificadoDigital': 'Certificado digital',
        'certificado.msgCarregandoCertificado': 'Carregando certificados...',
        'certificado.msgNenhumCertificadoEncontrado': 'Nenhum certificado encontrado',
        'certificado.msgErroCarregarCertificado': 'Erro ao carregar certificados',
        'certificado.msgCertificadoExpirado': '[Expirado]',
        'certificado.msgCertificadoNaoValido': '[Ainda não válido]',
        'certificado.msgCertificadoNaoIcpBrasil': '[Não ICP-Brasil]',
        'certificado.tituloProblemasAoAssinar': 'Falha de comunicação com o dispositivo de assinatura digital',

        'label.contato': 'Contato',
        'label.identificarSe': 'Identificar-se ',

        'mensagem.aguarde': 'Por favor, aguarde.',
        'mensagem.paginaNaoCarregada': 'Não foi possível carregar a página.',
        'mensagem.marcarLido': 'Marcar como lido',
        'mensagem.registrosSelecionados': 'Registros selecionados',
        'mensagem.registroJaSelecionado': 'Este registro já está selecionado',

        'mensagem.data.invalida': 'A data digitada é inválida.',
        'mensagem.data.anoInvalido': 'O ano informado deve ser maior que',
        'mensagem.data.mesInvalido': 'O mês não pode ser maior que 12.',
        'mensagem.data.mes': 'O mês',
        'mensagem.data.mesMaior29dias': 'não pode ter mais que 29 dias.',
        'mensagem.data.mesMaior28dias': 'não pode ter mais que 28 dias.',
        'mensagem.data.mesMaior31dias': 'não pode ter mais que 31 dias.',
        'mensagem.data.mesMaior30dias': 'não pode ter mais que 30 dias.',

        'mensagem.email.invalido': 'O formato do endereço de e-mail não é válido. Verifique se ele tem o formato "usuario@dominio".',
        'mensagem.email.caracteresInvalidos': 'O endereço de e-mail possui caracteres inválidos',
        'mensagem.email.usuarioInvalido': 'O formato do usuário informado no endereço de e-mail não é válido.',
        'mensagem.email.ipInvalido': 'O endereço IP informado no endereço de e-mail não é válido.',
        'mensagem.email.dominioInvalido': 'O formato do domínio informado no endereço de e-mail não é válido.',
        'mensagem.email.dominioIncompleto': 'O domínio informado no endereço de e-mail deve possuir pelo menos duas partes. Por exemplo: "usuario@empresa.com.br".',

        'mensagem.texto.tamanhoInvalido': 'O tamanho do texto digitado é maior do que o tamanho permitido. Tamanho permitido:',
        'mensagem.texto.caracter': 'O caracter',
        'mensagem.texto.caracterPosicaoInvalida': 'não está permitido na posição',

        'mensagem.numero.numeroInvalido': 'O valor digitado não é um número válido.',
        'mensagem.numero.numeroNaoPodeCasasDecimais': 'O número não pode conter casas decimais',
        'mensagem.numero.numeroCasaDecimaisInvalidas': 'O número de casas decimais é inválido. O número pode conter apenas',
        'mensagem.numero.casaDecimais': 'casas decimais',
        'mensagem.numero.numeroInteiroInvalido': 'O número de dígitos inteiros é inválido. O número pode conter apenas',
        'mensagem.numero.digitosInteiros': 'dígitos inteiros',
        'mensagem.numero.numeroTamanhoInvalido': 'O número digitado não pode ser maior que',
        'mensagem.numero.numeroZeroInvalido': 'O número digitado deve ser diferente de zero.'
    }
</script>



<script>
    var appEsajLayout = appEsajLayout || {};
    appEsajLayout.urlNovoMenuHtml = 'https://www2.tjal.jus.br/esaj/menuPortalV2Html.do?servico=190301';

    var appEsajCas = appEsajCas || {};
    appEsajCas.urlServicoConteudoIdentificacao = 'https://www2.tjal.jus.br/sajcas/conteudoIdentificacaoJson?script=1689231781289&retorno=' + encodeURIComponent(location.href);
</script>
<script src="https://www2.tjal.jus.br/esaj/js/portalV2-bundle.js?n=806192629"></script>

<script src="https://www2.tjal.jus.br/sajcas/seletorVersaoBeta.js?n=cf11148e-e81a-405e-9a9a-d6579880c0c7&amp;versao=2"></script>

    




        
            
                
                    
                
                
                

                

                

                

                

                
                
                
            
        
            
                
                
                

                

                

                

                

                
                    



















<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Apensos / Vinculados</h2>
        
    
</div>
    <!--  Tabela de (apensos) -->
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
        
            
            
                <tbody><tr>
                     <td colspan="3" align="left" id="dadosApensosNaoDisponiveis">Não há processos apensos ou vinculados para este processo.</td>
                </tr>
            
        
    </tbody></table>
    <!-- Tabela de (apensos) -->
    

                
                
                
            
        
            
                
                
                

                

                

                

                

                
                
                    




















<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Números de 1ª Instância</h2>
        
    
</div>


<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
  
    
      <tbody><tr class="label"> 
        <td align="left" valign="top" width="200">Nº de 1ª instância</td>
        <td align="left" valign="top" width="250">Foro</td>
        <td align="left" valign="top" width="200">Vara</td>
        <td align="left" valign="top" width="250">Juiz</td>
        <td align="left" valign="top" width="*">Obs.</td>
      </tr>
      <tr class="fundoEscuro" height="2">
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
    
    
  
</tbody></table>



<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    
      <tbody><tr class="fundoClaro"> 
        <td align="left" valign="top" width="200">
            
                
                    <a href="https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000" target="_blank">0710802-55.2018.8.02.0001</a> (Principal)
                
                
            
        </td>
        <td align="left" valign="top" width="250">
          Foro de Maceió
        </td>
        <td align="left" valign="top" width="200">
          4ª Vara Cível da Capital
        </td>
        <td align="left" valign="top" width="250">
          José Cícero Alves da Silva
        </td>
        <td align="left" valign="top">
          -
        </td>
      </tr>
            
</tbody></table>

                
                
            
        
            
                
                
                    
























<div style="padding-top: 10px;">
    
    
        
        
        
        
    

    
        
        
            <h2 class="subtitle">Partes do Processo</h2>
        
    
</div>

<!--  cabecalho da tabela de lista (partes) -->


<!--  dados da lista partes principais (partes) -->
<table id="tablePartesPrincipais" style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
    
            







    
        
    
    
    
    


<tbody><tr class="fundoClaro poloAtivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelante:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  Cony Engenharia Ltda.
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Carlos Henrique de Mendonça Brandão
              
          
          <input type="hidden" value="6770AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Guilherme Freire Furtado
              
          
          <input type="hidden" value="14781AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogada:&nbsp;</span>
          
              
              
                  Maria Eugênia Barreiros de Mello
              
          
          <input type="hidden" value="14717AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Vítor Reis de Araujo Carvalho
              
          
          <input type="hidden" value="14928AL">&nbsp;
         
      
      
     </td>
</tr>

    
            







    
    
        
    
    
    


<tr class="fundoClaro poloPassivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelado:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  José Carlos Cerqueira Souza Filho
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Vinicius Faria de Cerqueira
              
          
          <input type="hidden" value="9008AL">&nbsp;
         
      
      
     </td>
</tr>

    
</tbody></table>	


    <!--  dados da lista todas as partes (partes) -->
    <table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0">
        
            







    
        
    
    
    
    


<tbody><tr class="fundoClaro poloAtivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelante:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  Cony Engenharia Ltda.
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Carlos Henrique de Mendonça Brandão
              
          
          <input type="hidden" value="6770AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Guilherme Freire Furtado
              
          
          <input type="hidden" value="14781AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogada:&nbsp;</span>
          
              
              
                  Maria Eugênia Barreiros de Mello
              
          
          <input type="hidden" value="14717AL">&nbsp;
         
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Vítor Reis de Araujo Carvalho
              
          
          <input type="hidden" value="14928AL">&nbsp;
         
      
      
     </td>
</tr>

        
            







    
        
    
    
    
    


<tr class="fundoClaro poloAtivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelante:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  Banco do Brasil S A
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Nelson Wilians Fratoni Rodrigues
              
          
          <input type="hidden" value="9395AAL">&nbsp;
         
      
      
     </td>
</tr>

        
            







    
    
        
    
    
    


<tr class="fundoClaro poloPassivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelado:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  José Carlos Cerqueira Souza Filho
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Vinicius Faria de Cerqueira
              
          
          <input type="hidden" value="9008AL">&nbsp;
         
      
      
     </td>
</tr>

        
            







    
    
        
    
    
    


<tr class="fundoClaro poloPassivo">
    <td valign="top" width="141" style="padding-bottom: 5px" class="label">
      <span class="mensagemExibindo tipoDeParticipacao">Apelada:&nbsp;</span>
    </td>
    <td width="*" align="left" style="padding-bottom: 5px" class="nomeParteEAdvogado">
      
          
              
              
                  Livia Nascimento da Rocha
              
          
         
      
      
      
         <br><span class="mensagemExibindo">Advogado:&nbsp;</span>
          
              
              
                  Vinicius Faria de Cerqueira
              
          
          <input type="hidden" value="9008AL">&nbsp;
         
      
      
     </td>
</tr>

        
    </tbody></table>
    <div id="divLinksTituloBlocoPartes" style="text-align:right">
        







<input id="mensagemNaoExibidapartes" type="hidden" value="">
<input id="linkNaoExibidopartes" type="hidden" value="<span id=&quot;setasDireitapartes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

<span id="mensagensExibindopartes" class="mensagemExibindo">

</span> &nbsp;
<a id="linkpartes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
    <span id="setasDireitapartes" class="setasDireita">
        <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
    </span>
    Mais</a>

<script>
    $(function() {
        var controlarLink = function() {
            var $linkNaoExibido = $('input#linkNaoExibidopartes');
            var conteudoLinkNaoApresentado = $linkNaoExibido.val();
            var $link = $('a#linkpartes');

            $linkNaoExibido.val($link.html());
            $link.html(conteudoLinkNaoApresentado);
        };

        var controlarMensagem = function() {
            var $mensagemNaoExibida = $('input#mensagemNaoExibidapartes');
            var $spanMensagem = $('span#mensagensExibindopartes');
            var mensagemExibida = $spanMensagem.html();
            var mensagemNaoExibida = $mensagemNaoExibida.val();

            $spanMensagem.html(mensagemNaoExibida);
            $mensagemNaoExibida.val(mensagemExibida);
        };

        var controlarMensagemLink = function() {
            controlarMensagem();
            controlarLink();
        };

        var esconderElementosExtrasMostrarDefault = function() {
            $('#tableTodasPartes').hide();
            $('#tablePartesPrincipais').show();
        };

        var mostrarElementosExtrasEsconderDefault = function() {
            $('#tablePartesPrincipais').hide();
            $('#tableTodasPartes').show();
        };

        var initPagina = function() {
            var setasDireita = '<span id="setasDireitapartes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
            var $linkEscondido = $('input#linkNaoExibidopartes');
            $linkEscondido.val(setasDireita+$linkEscondido.val());
        };

        var bindLink = function() {
            var $link = $('a#linkpartes');
            $link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
            $link.bind('click', controlarMensagemLink);
        };

        initPagina();
        bindLink();
        esconderElementosExtrasMostrarDefault();
    });
</script>

    </div>


                
                

                

                

                

                

                
                
                
            
        
            
                
                
                

                

                

                
                    


  























<div style="padding-top: 10px;">
    
    
        
        
        
        
    

    
        
        
            <h2 class="subtitle">Movimentações</h2>
        
    
</div>

 
    

<table style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
    
        
            <thead>
                <tr> 
                  <th width="120" class="label" style="vertical-align: bottom">Data</th>
                  <th valign="middle" width="20" aria-hidden="true">&nbsp;</th>
                  <th valign="middle" class="label">Movimento</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </thead>

            
            <tbody id="tabelaUltimasMovimentacoes">
                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=88" name="M" cddocumento="88">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=88" name="M" cddocumento="88">
                    Certidão de Envio ao 1º Grau
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Faço remessa dos presentes autos à Origem.</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Baixa Definitiva
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=86" name="M" cddocumento="86">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=86" name="M" cddocumento="86">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">TERMO DE BAIXA Faço baixar estes autos ao Exmo(a). Juiz(a) de Direito da 4ª Vara Cível da Capital, em cumprimento ao despacho de página 872. Maceió, 26 de abril de 2023. Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Cícera Cristina Lima de Araújo Bandeira Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        12/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        12/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=84" name="M" cddocumento="84">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=84" name="M" cddocumento="84">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 12 de abril de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários</span>

        
    </td>
</tr>



                
            </tbody>
            
            
            <tbody style="display: none;" id="tabelaTodasMovimentacoes">
                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=88" name="M" cddocumento="88">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=88" name="M" cddocumento="88">
                    Certidão de Envio ao 1º Grau
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Faço remessa dos presentes autos à Origem.</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Baixa Definitiva
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=86" name="M" cddocumento="86">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=86" name="M" cddocumento="86">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">TERMO DE BAIXA Faço baixar estes autos ao Exmo(a). Juiz(a) de Direito da 4ª Vara Cível da Capital, em cumprimento ao despacho de página 872. Maceió, 26 de abril de 2023. Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Cícera Cristina Lima de Araújo Bandeira Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        12/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        12/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=84" name="M" cddocumento="84">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=84" name="M" cddocumento="84">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 12 de abril de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        11/04/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=83" name="M" cddocumento="83">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=83" name="M" cddocumento="83">
                    Proferido despacho de mero expediente
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Orlando Rocha Filho Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DESPACHO Cotejando os autos, observa-se que o Superior Tribunal de Justiça não acolheu a insurgência recursal (cf. fls. 863-867), tendo a respectiva Decisão transitado em julgado, e sendo mantido, assim, o Acórdão desta Corte Estadual. Diante disso, proceda-se à devida baixa dos autos ao Juízo de origem, atentando-se às formalidades de praxe. Publique-se. Intimem-se. Maceió/AL, 10 de abril de 2023. Desembargador Orlando Rocha Filho Vice-Presidente do Tribunal de Justiça de Alagoas</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        23/03/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Concluso à Vice - Presidência
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        23/03/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=81" name="M" cddocumento="81">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=81" name="M" cddocumento="81">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Faço estes autos conclusos ao Excelentíssimo Senhor Vice Presidente do Tribunal de Justiça de Alagoas. Maceió, 23 de março de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Andréia Maria Oliveira da Silva Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        23/03/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Decisão dos Tribunais Superiores
            
        

        

        <br>
        <span style="font-style: italic;">...conheço do agravo para negar provimento ao recurso especial</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        23/03/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Volta do STJ
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        18/01/2023
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo Transferido
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        10/11/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo enviado STJ
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        10/11/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        10/11/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        31/10/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        31/10/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=73" name="M" cddocumento="73">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=73" name="M" cddocumento="73">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 31 de outubro de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/10/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=71" name="M" cddocumento="71">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=71" name="M" cddocumento="71">
                    Recebido o recurso Sem efeito suspensivo
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DECISÃO 1. Nos termos do art. 1.042, §4º, do Código de Processo Civil, e tendo em vista não concordar com os argumentos suscitados pela parte agravante, mantenho a decisão recorrida por seus próprios fundamentos bem como determino, por conseguinte, a remessa dos autos ao Superior Tribunal de Justiça, para o regular processamento do Recurso Especial. Publique-se. Intimem-se. Cumpra-se. Maceió/AL, 27 de outubro de 2022. Desembargador Des. José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/10/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Concluso à Vice - Presidência
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        26/10/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=69" name="M" cddocumento="69">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=69" name="M" cddocumento="69">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">CERTIFICO que decorreu o prazo para o(a) recorrido(a) ou agravado(a) apresentar as contrarrazões ao recurso interposto. CERTIFICO, finalmente, que faço CONCLUSÃO dos autos ao Relator Des. José Carlos Malta Marques, Vice-Presidente.</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        30/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        30/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=67" name="M" cddocumento="67">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=67" name="M" cddocumento="67">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 30 de setembro de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        28/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=66" name="M" cddocumento="66">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=66" name="M" cddocumento="66">
                    Proferido despacho de mero expediente
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DESPACHO 1.Determino que seja intimada a parte agravada para que esta, querendo, apresente contrarrazões ao recurso interposto, observado o prazo legal contido no art. 1.042, § 3º, do Código de Processo Civil. 2. Cumpridas as formalidades de praxe, retornem os autos conclusos, para os fins do art. 1.042, § 4º, também do CPC. Publique-se. Intimem-se. Maceió/AL, 27 de setembro de 2022. Desembargador Des. José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        21/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Concluso à Vice - Presidência
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        21/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=64" name="M" cddocumento="64">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=64" name="M" cddocumento="64">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">CONCLUSÃO Faço estes autos conclusos ao Excelentíssimo Senhor Des. José Carlos Malta Marques, Vice - Presidente. Maceió, 21 de setembro de 2022 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        21/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=63" name="M" cddocumento="63">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=63" name="M" cddocumento="63">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">CERTIDÃO Certifico que foi interposto Agravo em Recurso Especial, como petição, em face da decisão de páginas 832-834, a qual inadmitiu o recurso. Maceió, 21 de setembro de 2022 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        21/09/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70032323-8
Tipo da Petição: Agravo de Instrumento em Recurso Especial
Data: 21/09/2022 11:03
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        31/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        31/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=59" name="M" cddocumento="59">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=59" name="M" cddocumento="59">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 31 de agosto de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        29/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=57" name="M" cddocumento="57">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=57" name="M" cddocumento="57">
                    Recurso Especial não admitido
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Recorrente: Cony Engenharia Ltda. Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Recorrido: José Carlos Cerqueira Souza Filho e outra Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL) DECISÃO 1. Trata-se de recurso especial interposto por Cony Engenharia Ltda., com fulcro no art. 105, inciso III, alínea a , da Constituição Federal/88, contra acórdão proferido pela 2ª Câmara Cível desta Corte de Justiça. 2. O recorrente, em suas razões recursais, às fls. 760/771, aduziu que o acórdão impugnado teria violado o artigo 1022, inciso II, do Código de Processo Civil. 3. Devidamente intimado, o recorrido ofertou contrarrazões ao recurso às fls. 809/814. 4. Em seguida, retornaram os autos conclusos para juízo de admissibilidade. 5.É, em síntese, o relatório. Fundamento e decido. 6.Entendo ser importante esclarecer que a competência jurisdicional desta Vice-Presidência, de acordo com o Código de Processo Civil, com o Regimento Interno do TJAL e com o Ato Normativo nº 03/2021, da Presidência deste Sodalício, resume-se à realização do juízo de admissibilidade de recursos especiais e extraordinários e ao processamento de incidentes relacionados a tais feitos, não se confundindo com a realização de juízo de mérito dos referidos recursos, exceto naquilo em que autorizado pelo art. 1.030, incisos I e II, do Código de Processo Civil (juízo de conformidade). 7.Cumpre notar, de pronto, o preenchimento dos requisitos genéricos, objetivos e subjetivos de admissibilidade do presente recurso especial, porquanto comprovada sua tempestividade, cabimento, regularidade formal, legitimidade das partes, interesse de agir, preparo e inexistência de fato impeditivo ou extintivo do poder de recorrer. 8.Outrossim, consoante é cediço, a interposição dos recursos excepcionais pressupõe o esgotamento das vias ordinárias. Sendo assim, os recursos extraordinário e especial implicam a existência de um julgado contra o qual já foram esgotadas as possibilidades de impugnação na instância ordinária, requisito este que se encontra preenchido no presente caso. 9.Seguindo com as exigências legais, necessário se faz demonstrar uma das hipóteses constitucionais de cabimento autorizadoras de seu manejo, in casu, alegou o recorrente que o presente recurso merece ser acolhido porque preenche os requisitos previstos no artigo 105, inciso III, alínea "a" da Constituição Federal. 10.Pois bem. Passo a analisá-lo. 11. A defesa do recorrente, nas razões recursais, sustentou a existência de violação ao artigo 1022, inciso II, do Código de Processo Civil. 12.Ocorre que tal alegação possui natureza procrastinatória e pugna, na verdade, pela instauração de nova discussão meritória, analisar a existência de suposta ofensa, importa, necessariamente, em revolvimento de matéria fático-probatória, o que é expressamente vedado pela Súmula n° 7, do Superior Tribunal de Justiça. Vejamos o teor da referida Súmula: STJ - Súmula n.º 7 - 28/06/1990 - DJ 03.07.1990 Reexame de Prova - Recurso Especial A pretensão de simples reexame de prova não enseja recurso especial. (grifos aditados) 13.Com efeito, a tese do recorrente, amparada na alegação de existência de ofensa ao mencionado dispositivo legal, é incompatível com a natureza excepcional do recurso especial, vez que o Tribunal ad quem teria que reavaliar os fatos e provas do processo. 14.A par de tais considerações, portanto, observo que os requisitos essenciais do artigo 105, inciso III, alínea "a", da Constituição Federal, não se encontram devidamente preenchidos. 15. Ante o exposto, inadmito o recurso especial. 16. Transitada em julgado, remetam-se os autos ao Juízo de origem para que sejam adotadas as providências cabíveis. Publique-se. Intimem-se. Cumpra-se. Maceió/AL, 29 de agosto de 2022 Desembargador José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        24/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Enviado para análise do Juízo de Admissibilidade RESP/RE
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70028500-0
Tipo da Petição: Petição
Data: 22/08/2022 16:12
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70028500-0
Tipo da Petição: Petição
Data: 22/08/2022 16:12
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/08/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70028500-0
Tipo da Petição: Petição
Data: 22/08/2022 16:12
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        06/06/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Enviado para análise do Juízo de Admissibilidade RESP/RE
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        03/06/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70018679-6
Tipo da Petição: Contrarrazões
Data: 03/06/2022 15:26
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        01/06/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Concluso à Vice - Presidência
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        31/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=49" name="M" cddocumento="49">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=49" name="M" cddocumento="49">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">CONCLUSÃO Faço estes autos conclusos ao Excelentíssimo Senhor Des. José Carlos Malta Marques, Vice - Presidente. Maceió, 30 de maio de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        30/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Interposto Recurso Especial
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        30/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Realizada Alteração de Relatoria
            
        

        

        <br>
        <span style="font-style: italic;">Orgão Julgador Anterior: 2ª Câmara Cível
Orgão Julgador Novo: Vice-Presidência

Relator Anterior: Des. Otávio Leão Praxedes
Relator Novo: Des. José Carlos Malta Marques

Motivo da alteração: recurso especial</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        30/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo Redistribuído
            
        

        

        <br>
        <span style="font-style: italic;">Antigo órgão julgador: 2ª Câmara Cível
Antigo relator: Des. Otávio Leão Praxedes</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Encaminhado para secretaria da Vice-Presidência
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=43" name="M" cddocumento="43">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=43" name="M" cddocumento="43">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Otávio Leão Praxedes Apelante : Cony Engenharia Ltda.. Advogado : Carlos Henrique de Mendonça Brandão (6770/AL). Advogada : Maria Eugênia Barreiros de Mello (14717/AL). Advogado : Vítor Reis de Araujo Carvalho (14928/AL). Advogado : Guilherme Freire Furtado (14781/AL). Apelante : Banco do Brasil S A. Advogado : Nelson Wilians Fratoni Rodrigues (9395A/AL). Apelado : José Carlos Cerqueira Souza Filho. Advogado : Vinicius Faria de Cerqueira (9008/AL). Apelada : Livia Nascimento da Rocha. Advogado : Vinicius Faria de Cerqueira (9008/AL) CERTIDÃO DE JUNTADA E REMESSA À SECRETARIA DA VICE-PRESIDÊNCIA Certifico, para os devidos fins, a juntada, nos presentes autos, do(s) incidente(s) de n.º : 0710802-55.2018.8.02.0001/50000 às páginas 776/806. Certifico, ainda, que decorreu o prazo legal sem que as demais partes interpusessem quaisquer incidentes e/ou recursos pertinentes à(o) Decisão/Acórdão retro. Certifico por último que faço remessa, nesta data, à Secretaria da Vice-Presidência, pois a(s) parte(s) Cony Engenharia Ltda. interpôs/interpuseram Recurso Especial às páginas 760/771. O referido é verdade e dou fé. Maceió, 27 de maio de 2022. Carla Christini Barros Costa de Oliveira Secretário(a) da 2ª Câmara Cível Luiz Carlos Maciel Rodrigues Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Certidão Emitida
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=28" name="M" cddocumento="28">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=28" name="M" cddocumento="28">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Apelação Cível nº 0710802-55.2018.8.02.0001 Relator :Des. Otávio Leão Praxedes Apelante: Cony Engenharia Ltda.. Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL). Advogada: Maria Eugênia Barreiros de Mello (OAB: 14717/AL). Advogado: Vítor Reis de Araujo Carvalho (OAB: 14928/AL). Advogado: Guilherme Freire Furtado (OAB: 14781/AL). Apelante: Banco do Brasil S A. Advogado: Nelson Wilians Fratoni Rodrigues (OAB: 9395A/AL). Apelado: José Carlos Cerqueira Souza Filho. Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL). Apelada: Livia Nascimento da Rocha. Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL). CERTIDÃO DE JUNTADA Junto, nesta data, aos presentes autos, os documentos pertinentes ao(s) Incidente(s) n.º 0710802-55.2018.8.02.0001/50000. Maceió,27 de maio de 2022. Carla Christini Barros Costa de Oliveira 2ª Câmara Cível Luiz Carlos Maciel Rodrigues Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        25/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70016995-6
Tipo da Petição: Recurso Especial Cível
Data: 25/05/2022 10:47
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        25/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70016995-6
Tipo da Petição: Recurso Especial Cível
Data: 25/05/2022 10:47
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        25/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Documento
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70016995-6
Tipo da Petição: Recurso Especial Cível
Data: 25/05/2022 10:47
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        25/05/2022
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.22.70016995-6
Tipo da Petição: Recurso Especial Cível
Data: 25/05/2022 10:47
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Protocolo nº WTRJ.2170030289-2 Embargos de Declaração Cível</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Incidente Cadastrado
            
        

        

        <br>
        <span style="font-style: italic;">Seq.: 50 - Embargos de Declaração Cível</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        13/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        13/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=18" name="M" cddocumento="18">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=18" name="M" cddocumento="18">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Otávio Leão Praxedes Apelante: Cony Engenharia Ltda.Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL)Advogada: Maria Eugênia Barreiros de Mello (OAB: 14717/AL)Advogado: Vítor Reis de Araujo Carvalho (OAB: 14928/AL)Advogado: Guilherme Freire Furtado (OAB: 14781/AL)Apelante: Banco do Brasil S AAdvogado: Nelson Wilians Fratoni Rodrigues (OAB: 9395A/AL)Apelado: José Carlos Cerqueira Souza FilhoAdvogado: Vinicius Faria de Cerqueira (OAB: 9008/AL)Apelada: Livia Nascimento da RochaAdvogado: Vinicius Faria de Cerqueira (OAB: 9008/AL) CERTIDÃO DE DISPONIBILIZAÇÃO DO ACÓRDÃO CERTIFICO, que foi disponibilizado no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas em 13/10/2021 e considerado publicado em 14/10/2021 a conclusão do venerando Acórdão julgado em 07/10/2021, nos termos do Artigo 943, § 2º do Código de Processo Civil c/c o artigo 4º, § 3º, da Lei nº 11.419/2006. Maceió/AL, 13 de outubro de 2021 Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível Gabrielle Wanderley Tenório Cavalcante Analista Judiciário</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        07/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=16" name="M" cddocumento="16">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=16" name="M" cddocumento="16">
                    Conhecido o recurso de
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Vistos, relatados e discutidos estes autos do Recurso de Apelação Cível nº 0710802-55.2018.8.02.0001, em que figuram, como parte apelante, Cony Engenharia LTDA e Banco do Brasil S/A; e, como parte apelada, José Carlos Cerqueira Souza Filho e Livia Nascimento da Rocha, ACORDAM, os Desembargadores integrantes desta 2ª Câmara Cível do Tribunal de Justiça do Estado de Alagoas, à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. Participaram do julgamento os eminentes Desembargadores constantes na Certidão de Julgamento.</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        07/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=15" name="M" cddocumento="15">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=15" name="M" cddocumento="15">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">Certifico que a 2ª Câmara Cível, assim decidiu: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator.. Participaram do julgamento: Juiz Conv. Carlos Cavalcanti de Albuquerque Filho, Des. João Luiz Azevedo Lessa, concovado em face das férias da Desa. Elisabeth Carvalho Nascimento e Des. Otávio Leão Praxedes. Presidiu a sessão o Exmo. Senhor Des. Otávio Leão Praxedes. Para constar lavro a presente certidão, do que dou fé. Maceió, 07 de outubro de 2021. Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        07/10/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo Julgado
            
        

        

        <br>
        <span style="font-style: italic;">à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. </span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        27/09/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=13" name="M" cddocumento="13">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=13" name="M" cddocumento="13">
                    Certidão Emitida
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">CERTIDÃO Certifico que o presente processo foi incluído na pauta de julgamento do dia 07 de outubro de 2021 às 9:00h, disponibilizado no Diário de Justiça Eletrônico no dia 27 de setembro de 2021, nos termos dos art. 6º da Resolução n.º 318/20 do CNJ, tendo sido a mesma afixada no mural informativo jurisdicional desta Corte de Justiça. Obs.: Em cumprimento a Resolução n. 13/2020, e ao art 1º do Ato Normativo n. 13/2021 disponibilizado no Diário de Justiça Eletrônico em 07/07/2021, as inscrições para sustentações orais deverão ser feitas EXCLUSIVAMENTE pelo sítio do Tribunal de Justiça (http://sadv.tjal.jus.br/login). Em caso de adiamento do julgamento, o advogado terá que realizar nova inscrição e credenciamento pelo portal. Maceió, 27 de setembro de 2021 Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        24/09/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Inclusão em pauta
            
        

        

        <br>
        <span style="font-style: italic;">Para 07/10/2021</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        23/09/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Publicado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/09/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=10" name="M" cddocumento="10">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=10" name="M" cddocumento="10">
                    Solicitação de dia para Julgamento - Relator
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;">DESPACHO Trata-se de dois Recursos de Apelação Cível, o primeiro interposto pelo Banco do Brasil S/A, às págs. 668/689, e o segundo interposto pela Cony Engenharia LTDA, às págs. 693/701, ambos em face da Sentença proferida pelo Juízo de Direito da 4ª Vara Cível da Capital, às págs. 649/663, que julgou parcialmente procedentes os pedidos da Ação Declaratória de Nulidade de Contrato de Financiamento Bancário c/c Indenização por Danos Materiais e Morais proposta por , às págs. 1/30, conforme se pode verificar no dispositivo abaixo transcrito: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a datada efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em danos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como corolário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se. (págs. 661/663 - Sem grifos no original). Em suas razões recursais, o Banco do Brasil S/A aduziu que: i) preliminarmente, é parte ilegítima para figurar no polo passivo da ação de origem, pois é mero agente financeiro e os descontos decorrentes do financiamento só iniciam após o "habite-se"; ii) a taxa de evolução de obra, também chamada de juros de obra, é cobrada nos financiamentos na modalidade créditos associativos para aquisição de imóveis na planta, mas o apelante não realiza esse tipo de cobrança, ele cobra apenas encargos adicionais, que correspondem aos juros devidos, tanto no período em que o imóvel ainda está na planta, quanto após o início do pagamento da parcela de amortização de capital; iii) a cobrança da referida taxa só se inicia após o "habite-se"; iii) o apelante não tem como acompanhar a evolução das milhares de obra que financia, cabendo à construtora comprovar que o "habite-se" foi liberado pela Prefeitura; iv) caso a apelada tivesse levado a cópia do "habite-se" à instituição financeira, o encargo já não seria mais cobrado; v) deve-se respeitar o princípio do pacta sunt servanda, pois o apelante apenas cumpriu o que foi determinado em contrato; vi) inexiste dever de indenizar, ante a ausência da prática de ato ilícito; e, vii) em caso de condenação ao pagamento de indenização por danos morais, o valor arbitrado não pode ensejar enriquecimento ilícito. Ao final, requereu o conhecimento e o provimento do presente Recurso de Apelação Cível, a fim de reformar a Sentença proferida pelo Juízo de Direito de Primeiro Grau, no sentido de julgar improcedentes os pedidos autorais; e, subsidiariamente, reduzir o valor arbitrado a título de indenização por danos morais. Por sua vez, a Cony Engenharia LTDA alegou que: i) a parte apelada sustenta que houve atraso na entrega de uma unidade imobiliária do empreendimento Dellavia Park Club; ii) o Juízo a quo entendeu que o atraso na entrega do imóvel seria incontroverso, o que necessariamente implicaria que a parte apelada teria deixado de auferir lucros a título de alugueis no período; iii) a presunção adotada pelo Juízo a quo de que o atraso na entrega do imóvel implica danos materiais, mais especificamente na modalidade de lucros cessantes, não é absoluta; iv) na petição inicial, a parte apelada afirma que o imóvel foi adquirido para sua própria moradia, de modo que nunca houve intenção de locação nem de auferir renda com o bem; v) as provas dos autos não deixam dúvidas sobre a finalidade de moradia da parte apelada e, por consequência, os supostos danos são meramente hipotéticos e sem correspondência com a realidade dos fatos; vi) o contrato de promessa de compra e venda foi celebrado unicamente pelo Sr. José Carlos Cerqueira, de modo que não há que se falar em danos morais à Sra. Livia Nascimento, já que não figurou como parte contratante com a empresa; vii) em relação aos supostos danos morais causados ao Sr. José Carlos Cerqueira, não houve violação a qualquer direito da personalidade; e vii) é válida a cláusula de tolerância de dezoito meses pactuada entre as partes e a aplicabilidade do INCC à correção do saldo devedor, não devendo prevalecer o entendimento do Juízo a quo pelo limite de tolerância de apenas cento e oitenta dias nem a substituição do índice pelo IGP-M para correção do saldo devedor. Por derradeiro, requereu o conhecimento e o provimento do presente Recurso de Apelação Cível, a fim de reformar a Sentença proferida pelo Juízo de Direito de Primeiro Grau, no sentido de julgar improcedentes os pedidos autorais; e, subsidiariamente, adotar a data de agosto de 2018 como referência para eventuais cálculos devidos e manter o INCC para correção do saldo devedor. Intimada a apresentar contrarrazões, a parte apelada alegou que: i) a preliminar de ilegitimidade passiva do Banco do Brasil S/A não merece prosperar, pois a presente lide diz respeito a negócios jurídicos diretamente ligados à instituição financeira, como a abusividade do contrato de financiamento, nulidade de cláusulas de financiamento e devolução das taxas de obra ilegalmente cobradas; a construtora não alegou em momento oportuno a preliminar de ilegitimidade passiva da Sra. Lívia Nascimento, sendo irrelevante qualquer argumento nesse sentido em sede recursal, por mais que o dano tenha sido evidenciado em razão da privação do bem sofrida juntamente com seu marido por tempo além do razoável; ii) a construtora só poderia fazer prova de que a mora contratual não lhe é imputável, mas não o fez; iii) os anos de espera e de expectativas, de frustrações, de chateações, de descontentamentos, discussões, mentiras e novas frustrações são suficientes para comprovar o dano moral; iv) a cláusula de tolerância de dezoito meses prevista no contrato afronta a jurisprudência do Superior Tribunal de Justiça, que já limitou o prazo de cento e oitenta dias; e v) o inadimplemento dos réus, em razão do atraso na entrega do imóvel, não pode gerar acréscimo ao saldo devedor, sob pena de onerar indevidamente o consumidor, pois transferiria os encargos da mora a quem não deu causa e mais, remunerando a construtora/incorporadora pelo próprio inadimplemento. Por fim, requereu o não provimento do Recurso de Apelação Cível, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau, apenas majorando os honorários advocatícios sucumbenciais. É, em síntese, o relatório. Estando o processo em ordem, peço inclusão na pauta de julgamento subsequente. Maceió, 22 de setembro de 2021 Des. Otávio Leão Praxedes Relator</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/07/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.21.70018896-8
Tipo da Petição: Petição
Data: 22/07/2021 16:32
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        25/05/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Juntada de Petição de
            
        

        

        <br>
        <span style="font-style: italic;">Nº Protocolo: WTRJ.21.70013501-5
Tipo da Petição: Petição Cível
Data: 25/05/2021 10:29
</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/02/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Concluso ao Relator
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/02/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
            <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=4" name="M" cddocumento="4">
                <img src="/cposg5/imagens/doc2.gif" width="16" height="16" border="0">
            </a>
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
                <a class="linkMovVincProc" title="Visualizar documento em inteiro teor" href="#?cdDocumento=4" name="M" cddocumento="4">
                    Termo de Distribuição Emitido
                </a>
            
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/02/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo Distribuído por Sorteio
            
        

        

        <br>
        <span style="font-style: italic;">Órgão Julgador: 2 - 2ª Câmara Cível
Relator: 86 - Des. Otávio Leão Praxedes</span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoEscuro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/02/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Processo Cadastrado
            
        

        

        <br>
        <span style="font-style: italic;"></span>

        
    </td>
</tr>



                
                    











    
    
        
    


<tr class="fundoClaro movimentacaoProcesso" style="">
    <td width="120" style="vertical-align: top" class="dataMovimentacaoProcesso">
        22/02/2021
    </td>
    <td width="20" valign="top" aria-hidden="true">
        
    </td>
    <td style="vertical-align: top; padding-bottom: 5px" class="descricaoMovimentacaoProcesso">
        

        
            
            
                Recebidos os Autos pela Entrada de Recursos
            
        

        

        <br>
        <span style="font-style: italic;">Foro de origem: Foro de Maceió
Vara de origem: 4ª Vara Cível da Capital</span>

        
    </td>
</tr>



                
            </tbody>

        
        
    
</table>


    <div id="divLinksTituloBlocoMovimentacoes" style="text-align:right">
        







<input id="mensagemNaoExibidamovimentacoes" type="hidden" value="">
<input id="linkNaoExibidomovimentacoes" type="hidden" value="<span id=&quot;setasDireitamovimentacoes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

<span id="mensagensExibindomovimentacoes" class="mensagemExibindo">

</span> &nbsp;
<a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
    <span id="setasDireitamovimentacoes" class="setasDireita">
        <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
    </span>
    Mais</a>

<script>
    $(function() {
        var controlarLink = function() {
            var $linkNaoExibido = $('input#linkNaoExibidomovimentacoes');
            var conteudoLinkNaoApresentado = $linkNaoExibido.val();
            var $link = $('a#linkmovimentacoes');

            $linkNaoExibido.val($link.html());
            $link.html(conteudoLinkNaoApresentado);
        };

        var controlarMensagem = function() {
            var $mensagemNaoExibida = $('input#mensagemNaoExibidamovimentacoes');
            var $spanMensagem = $('span#mensagensExibindomovimentacoes');
            var mensagemExibida = $spanMensagem.html();
            var mensagemNaoExibida = $mensagemNaoExibida.val();

            $spanMensagem.html(mensagemNaoExibida);
            $mensagemNaoExibida.val(mensagemExibida);
        };

        var controlarMensagemLink = function() {
            controlarMensagem();
            controlarLink();
        };

        var esconderElementosExtrasMostrarDefault = function() {
            $('#tabelaTodasMovimentacoes').hide();
            $('#tabelaUltimasMovimentacoes').show();
        };

        var mostrarElementosExtrasEsconderDefault = function() {
            $('#tabelaUltimasMovimentacoes').hide();
            $('#tabelaTodasMovimentacoes').show();
        };

        var initPagina = function() {
            var setasDireita = '<span id="setasDireitamovimentacoes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
            var $linkEscondido = $('input#linkNaoExibidomovimentacoes');
            $linkEscondido.val(setasDireita+$linkEscondido.val());
        };

        var bindLink = function() {
            var $link = $('a#linkmovimentacoes');
            $link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
            $link.bind('click', controlarMensagemLink);
        };

        initPagina();
        bindLink();
        esconderElementosExtrasMostrarDefault();
    });
</script>

    </div>

                

                

                
                
                
            
        
            
                
                
                

                
                    
























<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Incidentes, ações incidentais, recursos e execuções de sentenças</h2>
        
    
</div>
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    
        
            <tbody><tr class="label">
                <th width="140" style="text-align:left">
                    Recebido em
                </th>
                
                <th width="*">Classe</th>
            </tr>
            <tr class="fundoEscuro" height="2" aria-hidden="true">
                
                <td></td><td></td>
            </tr>
            
                <tr class="fundoClaro">
                    <td width="140" style="text-align:left">
                        21/10/2021
                    </td>
                    






<td width="*">
    <a href="/cposg5/show.do?processo.codigo=P00006BXP12KW&amp;uuidCaptcha=&amp;processo.foro=900" target="_top">
        Embargos de Declaração Cível
        
             - 50000
        
        
    </a>
</td>

                </tr>        
            
        
        
    
</tbody></table>
<!--  incidentes -->


                

                

                

                

                
                
                
            
        
            
                
                
                

                

                
                    




















<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Petições diversas</h2>
        
    
</div>
<!--  Tabela de petições diversas -->
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    
        
            <thead>
                <tr class="label"> 
                  <th width="140" style="text-align:left">Data</th>
                  <th width="*">Tipo</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td></td>
                    <td></td>
                </tr>
            </thead>
            <tbody>
                
                    <tr class="fundoClaro"> 
                        <td width="140" style="text-align:left">
                            25/05/2021
                        </td>
                        <td width="*">
                            Petição Cível<br>
                            
                        </td>
                    </tr>
                
                    <tr class="fundoEscuro"> 
                        <td width="140" style="text-align:left">
                            22/07/2021
                        </td>
                        <td width="*">
                            Petição<br>
                            
                        </td>
                    </tr>
                
                    <tr class="fundoClaro"> 
                        <td width="140" style="text-align:left">
                            25/05/2022
                        </td>
                        <td width="*">
                            Recurso Especial Cível<br>
                            
                        </td>
                    </tr>
                
                    <tr class="fundoEscuro"> 
                        <td width="140" style="text-align:left">
                            03/06/2022
                        </td>
                        <td width="*">
                            Contrarrazões<br>
                            
                        </td>
                    </tr>
                
                    <tr class="fundoClaro"> 
                        <td width="140" style="text-align:left">
                            22/08/2022
                        </td>
                        <td width="*">
                            Petição<br>
                            
                        </td>
                    </tr>
                
                    <tr class="fundoEscuro"> 
                        <td width="140" style="text-align:left">
                            21/09/2022
                        </td>
                        <td width="*">
                            Agravo de Instrumento em Recurso Especial<br>
                            
                        </td>
                    </tr>
                
            </tbody>
        
        
    
</table>
<!--  Tabela de petições diversas -->

                

                

                

                
                
                
            
        
            
                
                
                
                    













    







<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Composição do Julgamento</h2>
        
    
</div>
    
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
        <tbody><tr class="label"> 
          <td width="140">Participação</td>
          <td>Magistrado</td>
        </tr>
        <tr class="fundoEscuro" height="2">
            <td></td>
            <td></td>
        </tr>
    </tbody></table>
    
    
    
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
        
          <tbody><tr class="fundoClaro itemComposicaoJulgamento"> 
            <td valign="top" width="140" class="label" style="padding-bottom: 5px">
              Relator
            </td>
            <td valign="top" style="padding-bottom: 5px">
              Des. Otávio Leão Praxedes&nbsp;
            </td>
          </tr>
        
          <tr class="fundoEscuro itemComposicaoJulgamento"> 
            <td valign="top" width="140" class="label" style="padding-bottom: 5px">
              2º Julgador
            </td>
            <td valign="top" style="padding-bottom: 5px">
              Juiz Conv. Carlos Cavalcanti de Albuquerque Filho&nbsp;
            </td>
          </tr>
        
          <tr class="fundoClaro itemComposicaoJulgamento"> 
            <td valign="top" width="140" class="label" style="padding-bottom: 5px">
              3º Julgador
            </td>
            <td valign="top" style="padding-bottom: 5px">
              Desa. Elisabeth Carvalho Nascimento&nbsp;
            </td>
          </tr>
        
    </tbody></table>
    


                

                

                

                

                

                
                
                
            
        
            
                
                
                

                

                

                

                
                    




















<div style="padding-top: 10px;">
    
    
        
        
            <h2 class="subtitle">Julgamentos</h2>
        
    
</div>
<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
  
    
      <tbody><tr class="label"> 
        <td align="left" valign="top" width="150">Data</td>
        <td align="left" valign="top" width="220">Situação do julgamento</td>
        <td align="left" valign="top" width="*">Decisão</td>
      </tr>
      <tr class="fundoEscuro" height="2">
        <td></td>
        <td></td>
        <td></td>
      </tr>
    
    
  
</tbody></table>


<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
        
          <tbody><tr class="fundoClaro"> 
            <td valign="top" align="left" width="150">
              07/10/2021
            </td>
            <td align="left" valign="top" width="220" "="">
              Julgado
            </td>
            <td align="left" valign="top" width="*">
              à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator.
            </td>
          </tr>
        
</tbody></table>

                

                
                
                
            
        
        <br>
        <br>


    
        
    

    














    
    
        



<footer>
    <nav class="navbar__footer">
        <div class="navbar__footer__container">

            <ul class="navbar__footer__list-brand">
                <li class="navbar__footer__list-brand__item">
                    <a href="https://www.softplan.com.br/solucoes/saj-tribunais/" class="navbar__footer__list-brand__item__link link_softplan_tribunais">
                        <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-saj.png" alt="SAJ">
                    </a>
                </li>
                <li class="navbar__footer__list-brand__item">
                    <a href="https://www.softplan.com.br/" class="navbar__footer__list-brand__item__link link_softplan">
                        <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-softplan.png" alt="Softplan">
                    </a>
                </li>
            </ul>

            <ul class="navbar__footer__list-actions">
            </ul>
        </div>
    </nav>
</footer>

    





    

    </div>
    
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":113,"applicationID":"124655562","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfEgIdQBdEEBBDT1ZTRAgKXR0wXgoTcQJDWV8P","queueTime":0}</script>




<article style="z-index: 2147483647;"></article></body>
"""


@pytest.fixture
def mocked_html_1st():
    return mocked_html_1st_instance


@pytest.fixture
def mocked_html_2nd():
    return mocked_html_2nd_instance


def test_primary_data_crawler_1st_instance(mocked_html_1st):
    result = extract_primary_data_1st_instance(mocked_html_1st)

    assert result['Classe'] == 'Procedimento Comum Cível'
    assert result['Area'] == 'Cível'
    assert result['Assunto'] == 'Dano Material'
    assert result['Data de distribuicao'] == '02/05/2018 às 19:01 - Sorteio'
    assert result['Juiz'] == 'José Cícero Alves da Silva'
    assert result['Valor da acao'] == 'R$281.178,42'


def test_primary_data_crawler_2nd_instance(mocked_html_2nd):
    result = extract_primary_data_2nd_instance(mocked_html_2nd)

    assert result['Classe'] == 'Apelação Cível'
    assert result['Area'] == 'Cível'
    assert result['Assunto'] == 'Obrigações'
    assert result['Relator'] == 'VICE PRESIDENTE DO TRIBUNAL DE JUSTIÇA DE ALAGOAS'
    assert result['Valor da acao'] == '281.178,42'


def test_extract_parties_involved_1st_instance(mocked_html_1st):
    result = extract_parties_involved(mocked_html_1st)

    assert result['Autor'] == "José Carlos Cerqueira Souza Filho Advogado: Vinicius Faria de Cerqueira"
    assert result['Ré'] == "Cony Engenharia Ltda. Advogado: Carlos Henrique de Mendonça Brandão Advogado: Guilherme Freire Furtado Advogada: Maria Eugênia Barreiros de Mello Advogado: Vítor Reis de Araujo Carvalho"
    assert result['Autora'] == "Livia Nascimento da Rocha Advogado: Vinicius Faria de Cerqueira"
    assert result['Réu'] == "Banco do Brasil S A Advogado: Nelson Wilians Fratoni Rodrigues"


def test_extract_parties_involved_2nd_instance(mocked_html_2nd):
    result = extract_parties_involved(mocked_html_2nd)

    assert result['Apelante'] == 'Banco do Brasil S A Advogado: Nelson Wilians Fratoni Rodrigues'
    assert result['Apelado'] == "José Carlos Cerqueira Souza Filho Advogado: Vinicius Faria de Cerqueira"
    assert result['Apelada'] == "Livia Nascimento da Rocha Advogado: Vinicius Faria de Cerqueira"


def test_extract_legal_moviments_1st_instance(mocked_html_1st):
    result = extract_legal_moviments_1st_instance(mocked_html_1st)

    expected = [ { "05/05/2023": "Execução de Sentença Iniciada Seq.: 01 - Cumprimento de sentença" }, { "05/05/2023": "Ato Publicado Relação: 0282/2023 Data da Publicação: 08/05/2023 Número do Diário: 3296" }, { "04/05/2023": "Disponibilização no Diário da Justiça Eletrônico Relação: 0282/2023 Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto) Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)" }, { "04/05/2023": "Recebido pela Contadoria UNIFICADA" }, { "04/05/2023": "Ato Ordinatório - Artigo 162, §4º, CPC Ato Ordinatório- Remessa à contadoria" }, { "05/05/2023": "Execução de Sentença Iniciada Seq.: 01 - Cumprimento de sentença" }, { "05/05/2023": "Ato Publicado Relação: 0282/2023 Data da Publicação: 08/05/2023 Número do Diário: 3296" }, { "04/05/2023": "Disponibilização no Diário da Justiça Eletrônico Relação: 0282/2023 Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto) Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)" }, { "04/05/2023": "Recebido pela Contadoria UNIFICADA" }, { "04/05/2023": "Ato Ordinatório - Artigo 162, §4º, CPC Ato Ordinatório- Remessa à contadoria" }, { "04/05/2023": "Ato ordinatório praticado Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento: 25/05/2023" }, { "03/05/2023": "Transitado em Julgado" }, { "03/05/2023": "Recebimento da Instância Superior - Altera situação para \"Julgado\"" }, { "26/04/2023": "Recebido recurso eletrônico Data do julgamento: 07/10/2021 Trânsito em julgado: Tipo de julgamento: Acórdão Decisão: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. Situação do provimento: Relator: Des. Otávio Leão Praxedes" }, { "22/02/2021": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso" }, { "10/02/2021": "Juntada de Documento Nº Protocolo: WMAC.21.70031538-2 Tipo da Petição: Contrarrazões Data: 10/02/2021 19:27" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "06/01/2021": "Ato Publicado Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738" }, { "05/01/2021": "Disponibilização no Diário da Justiça Eletrônico Relação: 0003/2021 Teor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário Advogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)" }, { "04/01/2021": "Ato Ordinatório - Artigo 162, §4º, CPC Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário" }, { "18/12/2020": "Juntada de Documento Nº Protocolo: WMAC.20.70269584-0 Tipo da Petição: Juntada de Instrumento de Procuração Data: 18/12/2020 17:23" }, { "18/12/2020": "Juntada de Documento Nº Protocolo: WMAC.20.70269581-5 Tipo da Petição: Recurso de Apelação Data: 18/12/2020 17:18" }, { "15/12/2020": "Juntada de Documento Nº Protocolo: WMAC.20.70265228-8 Tipo da Petição: Recurso de Apelação Data: 15/12/2020 13:26" }, { "24/11/2020": "Ato Publicado Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711" }, { "24/11/2020": "Ato Publicado Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711" }, { "24/11/2020": "Ato Publicado Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711" }, { "24/11/2020": "Ato Publicado Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711" }, { "23/11/2020": "Disponibilização no Diário da Justiça Eletrônico Relação: 0912/2020 Teor do ato: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se. Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)" }, { "23/11/2020": "Julgado procedente em parte do pedido Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.Vencimento: 16/12/2020" }, { "23/09/2020": "Conclusos" }, { "16/08/2020": "Visto em Autoinspeção Despacho Visto em Autoinspeção" }, { "11/05/2020": "Juntada de Documento Nº Protocolo: WMAC.20.70092549-0 Tipo da Petição: Pedido de Andamento do proc./sent./decisões/desp. Data: 11/05/2020 13:28" }, { "10/12/2019": "Conclusos" }, { "11/11/2019": "Despacho de Mero Expediente DESPACHO Compulsando detidamente o feito, verifico que este inclui-se nos processos com prioridade de impulsionamento, consoante recomendação exarada pelo Conselho Nacional de Justiça, a qual determina a priorização de andamento das demandas paralisadas há mais de 100 (dias). Destarte, considerando que cada uma desses processos exige análise acurada por este magistrado a fim de que lhe seja dado efetivo provimento, determino a conclusão de todos os autos que se amoldem à hipótese alhures delineada - de competência do gabinete - para análise e devido impulsionamento, este especificamente, na fila concluso - impulso ao feito. Cumpra-se. Maceió(AL), 11 de novembro de 2019. José Cícero Alves da Silva Juiz de Direito" }, { "12/07/2019": "Juntada de Petição Nº Protocolo: WMAC.19.70150828-9 Tipo da Petição: Petição Data: 11/07/2019 23:50" }, { "12/02/2019": "Juntada de Petição Nº Protocolo: WMAC.19.70034823-7 Tipo da Petição: Petição Data: 12/02/2019 14:58" }, { "11/02/2019": "Juntada de Petição Nº Protocolo: WMAC.19.70032532-6 Tipo da Petição: Petição Data: 11/02/2019 09:13" }, { "06/12/2018": "Conclusos" }, { "05/12/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70259903-1 Tipo da Petição: Petição Data: 05/12/2018 16:46" }, { "29/11/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70255192-6 Tipo da Petição: Petição Data: 29/11/2018 15:07" }, { "28/11/2018": "Ato Publicado Relação :0499/2018 Data da Publicação: 29/11/2018 Número do Diário: 2233" }, { "27/11/2018": "Disponibilização no Diário da Justiça Eletrônico Relação: 0499/2018 Teor do ato: ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018 Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Rafael Sganzerla Durand (OAB 10132A/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)" }, { "27/11/2018": "Ato ordinatório praticado ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018" }, { "26/11/2018": "Juntada de Documento Nº Protocolo: WMAC.18.70251514-8 Tipo da Petição: Impugnação à Contestação Data: 26/11/2018 15:37" }, { "26/11/2018": "Juntada de Documento Nº Protocolo: WMAC.18.70251511-3 Tipo da Petição: Impugnação à Contestação Data: 26/11/2018 15:35" }, { "09/11/2018": "Ato Publicado Relação :0456/2018 Data da Publicação: 12/11/2018 Número do Diário: 2222" }, { "08/11/2018": "Disponibilização no Diário da Justiça Eletrônico Relação: 0456/2018 Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)" }, { "06/11/2018": "Ato ordinatório praticado Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista JudiciárioVencimento: 29/11/2018" }, { "16/10/2018": "Juntada de Documentos Nº Protocolo: WMAC.18.70221617-5 Tipo da Petição: Contestação Data: 16/10/2018 14:43" }, { "10/10/2018": "Juntada de Documentos Nº Protocolo: WMAC.18.70218154-1 Tipo da Petição: Contestação Data: 10/10/2018 14:04" }, { "24/09/2018": "Juntada de Documento" }, { "24/09/2018": "Juntada de Documento" }, { "24/09/2018": "Audiência Realizada Assentada - Genérico" }, { "24/09/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70203989-3 Tipo da Petição: Petição Data: 24/09/2018 10:09" }, { "21/09/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70203544-8 Tipo da Petição: Petição Data: 21/09/2018 18:07" }, { "21/09/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70203528-6 Tipo da Petição: Petição Data: 21/09/2018 17:42" }, { "21/09/2018": "Juntada de Petição Nº Protocolo: WMAC.18.70203260-0 Tipo da Petição: Petição Data: 21/09/2018 13:58" }, { "20/09/2018": "Visto em correição DESPACHO VISTO EM CORREIÇÃO" }, { "06/06/2018": "Juntada de AR - Cumprido Em 06 de junho de 2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente ao ofício n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário:" }, { "06/06/2018": "Juntada de AR - Cumprido Em 06 de junho de 2018 é juntado a estes autos o aviso de recebimento (AR803969745TJ - Cumprido), referente ao ofício n. 0710802-55.2018.8.02.0001-0001, emitido para Banco do Brasil S A. Usuário:" }, { "15/05/2018": "Ato Publicado Relação :0220/2018 Data da Publicação: 16/05/2018 Número do Diário: 2105" }, { "15/05/2018": "Ato Publicado Relação :0220/2018 Data da Publicação: 16/05/2018 Número do Diário: 2105" }, { "11/05/2018": "Disponibilização no Diário da Justiça Eletrônico Relação: 0220/2018 Teor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta \"taxa de obra\", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da \"taxa de obra\", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra. Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo. No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda. Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)" }, { "11/05/2018": "Disponibilização no Diário da Justiça Eletrônico Relação: 0220/2018 Teor do ato: Conciliação Data: 24/09/2018 Hora 14:00 Local: Sala de Audiência Situacão: Pendente Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)" }, { "11/05/2018": "Carta Expedida AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado" }, { "11/05/2018": "Carta Expedida AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado" }, { "11/05/2018": "Audiência Designada Conciliação Data: 24/09/2018 Hora 14:00 Local: Sala de Audiência Situacão: Realizada" }, { "10/05/2018": "Não Concedida a Antecipação de tutela DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta \"taxa de obra\", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da \"taxa de obra\", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra. Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo. No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda. Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de DireitoVencimento: 01/06/2018" }, { "03/05/2018": "Conclusos" }, { "02/05/2018": "Conclusos" }, { "02/05/2018": "Distribuído por Sorteio" } ]

    assert result == expected


def test_extract_legal_moviments_2nd_instance(mocked_html_2nd):
    result = extract_legal_moviments_2nd_instance(mocked_html_2nd)

    expected = [ { "26/04/2023": "Certidão de Envio ao 1º Grau Faço remessa dos presentes autos à Origem." }, { "26/04/2023": "Baixa Definitiva" }, { "26/04/2023": "Certidão Emitida TERMO DE BAIXA Faço baixar estes autos ao Exmo(a). Juiz(a) de Direito da 4ª Vara Cível da Capital, em cumprimento ao despacho de página 872. Maceió, 26 de abril de 2023. Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Cícera Cristina Lima de Araújo Bandeira Analista Judiciário" }, { "12/04/2023": "Publicado" }, { "12/04/2023": "Certidão Emitida Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 12 de abril de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários" }, { "26/04/2023": "Certidão de Envio ao 1º Grau Faço remessa dos presentes autos à Origem." }, { "26/04/2023": "Baixa Definitiva" }, { "26/04/2023": "Certidão Emitida TERMO DE BAIXA Faço baixar estes autos ao Exmo(a). Juiz(a) de Direito da 4ª Vara Cível da Capital, em cumprimento ao despacho de página 872. Maceió, 26 de abril de 2023. Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Cícera Cristina Lima de Araújo Bandeira Analista Judiciário" }, { "12/04/2023": "Publicado" }, { "12/04/2023": "Certidão Emitida Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 12 de abril de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários" }, { "11/04/2023": "Proferido despacho de mero expediente Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Orlando Rocha Filho Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DESPACHO Cotejando os autos, observa-se que o Superior Tribunal de Justiça não acolheu a insurgência recursal (cf. fls. 863-867), tendo a respectiva Decisão transitado em julgado, e sendo mantido, assim, o Acórdão desta Corte Estadual. Diante disso, proceda-se à devida baixa dos autos ao Juízo de origem, atentando-se às formalidades de praxe. Publique-se. Intimem-se. Maceió/AL, 10 de abril de 2023. Desembargador Orlando Rocha Filho Vice-Presidente do Tribunal de Justiça de Alagoas" }, { "23/03/2023": "Concluso à Vice - Presidência" }, { "23/03/2023": "Certidão Emitida Faço estes autos conclusos ao Excelentíssimo Senhor Vice Presidente do Tribunal de Justiça de Alagoas. Maceió, 23 de março de 2023 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários Andréia Maria Oliveira da Silva Analista Judiciário" }, { "23/03/2023": "Decisão dos Tribunais Superiores ...conheço do agravo para negar provimento ao recurso especial" }, { "23/03/2023": "Volta do STJ" }, { "18/01/2023": "Processo Transferido" }, { "10/11/2022": "Processo enviado STJ" }, { "10/11/2022": "Juntada de Documento" }, { "10/11/2022": "Certidão Emitida" }, { "31/10/2022": "Publicado" }, { "31/10/2022": "Certidão Emitida Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 31 de outubro de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência" }, { "27/10/2022": "Recebido o recurso Sem efeito suspensivo Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DECISÃO 1. Nos termos do art. 1.042, §4º, do Código de Processo Civil, e tendo em vista não concordar com os argumentos suscitados pela parte agravante, mantenho a decisão recorrida por seus próprios fundamentos bem como determino, por conseguinte, a remessa dos autos ao Superior Tribunal de Justiça, para o regular processamento do Recurso Especial. Publique-se. Intimem-se. Cumpra-se. Maceió/AL, 27 de outubro de 2022. Desembargador Des. José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas" }, { "26/10/2022": "Concluso à Vice - Presidência" }, { "26/10/2022": "Certidão Emitida CERTIFICO que decorreu o prazo para o(a) recorrido(a) ou agravado(a) apresentar as contrarrazões ao recurso interposto. CERTIFICO, finalmente, que faço CONCLUSÃO dos autos ao Relator Des. José Carlos Malta Marques, Vice-Presidente." }, { "30/09/2022": "Publicado" }, { "30/09/2022": "Certidão Emitida Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 30 de setembro de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência" }, { "28/09/2022": "Proferido despacho de mero expediente Agravo em Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Agravante : Cony Engenharia Ltda.. Advogados : Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Agravado : José Carlos Cerqueira Souza Filho. Advogados : Vinicius Faria de Cerqueira (OAB: 9008/AL) e outros DESPACHO 1.Determino que seja intimada a parte agravada para que esta, querendo, apresente contrarrazões ao recurso interposto, observado o prazo legal contido no art. 1.042, § 3º, do Código de Processo Civil. 2. Cumpridas as formalidades de praxe, retornem os autos conclusos, para os fins do art. 1.042, § 4º, também do CPC. Publique-se. Intimem-se. Maceió/AL, 27 de setembro de 2022. Desembargador Des. José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas" }, { "21/09/2022": "Concluso à Vice - Presidência" }, { "21/09/2022": "Certidão Emitida CONCLUSÃO Faço estes autos conclusos ao Excelentíssimo Senhor Des. José Carlos Malta Marques, Vice - Presidente. Maceió, 21 de setembro de 2022 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários" }, { "21/09/2022": "Certidão Emitida CERTIDÃO Certifico que foi interposto Agravo em Recurso Especial, como petição, em face da decisão de páginas 832-834, a qual inadmitiu o recurso. Maceió, 21 de setembro de 2022 Eleonora Paes Cerqueira de França Diretora Adjunta Especial de Assuntos Judiciários" }, { "21/09/2022": "Juntada de Petição de Nº Protocolo: WTRJ.22.70032323-8 Tipo da Petição: Agravo de Instrumento em Recurso Especial Data: 21/09/2022 11:03" }, { "31/08/2022": "Publicado" }, { "31/08/2022": "Certidão Emitida Certifico que foi disponibilizado(a) no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas, nesta data, o(a) Despacho/Decisão retro, nos termos do art 4º, § 3º, da Lei nº 11.419/2006. Maceió, 31 de agosto de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência" }, { "29/08/2022": "Recurso Especial não admitido Recurso Especial em Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. José Carlos Malta Marques Recorrente: Cony Engenharia Ltda. Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL) e outros Recorrido: José Carlos Cerqueira Souza Filho e outra Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL) DECISÃO 1. Trata-se de recurso especial interposto por Cony Engenharia Ltda., com fulcro no art. 105, inciso III, alínea a , da Constituição Federal/88, contra acórdão proferido pela 2ª Câmara Cível desta Corte de Justiça. 2. O recorrente, em suas razões recursais, às fls. 760/771, aduziu que o acórdão impugnado teria violado o artigo 1022, inciso II, do Código de Processo Civil. 3. Devidamente intimado, o recorrido ofertou contrarrazões ao recurso às fls. 809/814. 4. Em seguida, retornaram os autos conclusos para juízo de admissibilidade. 5.É, em síntese, o relatório. Fundamento e decido. 6.Entendo ser importante esclarecer que a competência jurisdicional desta Vice-Presidência, de acordo com o Código de Processo Civil, com o Regimento Interno do TJAL e com o Ato Normativo nº 03/2021, da Presidência deste Sodalício, resume-se à realização do juízo de admissibilidade de recursos especiais e extraordinários e ao processamento de incidentes relacionados a tais feitos, não se confundindo com a realização de juízo de mérito dos referidos recursos, exceto naquilo em que autorizado pelo art. 1.030, incisos I e II, do Código de Processo Civil (juízo de conformidade). 7.Cumpre notar, de pronto, o preenchimento dos requisitos genéricos, objetivos e subjetivos de admissibilidade do presente recurso especial, porquanto comprovada sua tempestividade, cabimento, regularidade formal, legitimidade das partes, interesse de agir, preparo e inexistência de fato impeditivo ou extintivo do poder de recorrer. 8.Outrossim, consoante é cediço, a interposição dos recursos excepcionais pressupõe o esgotamento das vias ordinárias. Sendo assim, os recursos extraordinário e especial implicam a existência de um julgado contra o qual já foram esgotadas as possibilidades de impugnação na instância ordinária, requisito este que se encontra preenchido no presente caso. 9.Seguindo com as exigências legais, necessário se faz demonstrar uma das hipóteses constitucionais de cabimento autorizadoras de seu manejo, in casu, alegou o recorrente que o presente recurso merece ser acolhido porque preenche os requisitos previstos no artigo 105, inciso III, alínea \"a\" da Constituição Federal. 10.Pois bem. Passo a analisá-lo. 11. A defesa do recorrente, nas razões recursais, sustentou a existência de violação ao artigo 1022, inciso II, do Código de Processo Civil. 12.Ocorre que tal alegação possui natureza procrastinatória e pugna, na verdade, pela instauração de nova discussão meritória, analisar a existência de suposta ofensa, importa, necessariamente, em revolvimento de matéria fático-probatória, o que é expressamente vedado pela Súmula n° 7, do Superior Tribunal de Justiça. Vejamos o teor da referida Súmula: STJ - Súmula n.º 7 - 28/06/1990 - DJ 03.07.1990 Reexame de Prova - Recurso Especial A pretensão de simples reexame de prova não enseja recurso especial. (grifos aditados) 13.Com efeito, a tese do recorrente, amparada na alegação de existência de ofensa ao mencionado dispositivo legal, é incompatível com a natureza excepcional do recurso especial, vez que o Tribunal ad quem teria que reavaliar os fatos e provas do processo. 14.A par de tais considerações, portanto, observo que os requisitos essenciais do artigo 105, inciso III, alínea \"a\", da Constituição Federal, não se encontram devidamente preenchidos. 15. Ante o exposto, inadmito o recurso especial. 16. Transitada em julgado, remetam-se os autos ao Juízo de origem para que sejam adotadas as providências cabíveis. Publique-se. Intimem-se. Cumpra-se. Maceió/AL, 29 de agosto de 2022 Desembargador José Carlos Malta Marques Vice-Presidente do Tribunal de Justiça de Alagoas" }, { "24/08/2022": "Enviado para análise do Juízo de Admissibilidade RESP/RE" }, { "22/08/2022": "Juntada de Documento Nº Protocolo: WTRJ.22.70028500-0 Tipo da Petição: Petição Data: 22/08/2022 16:12" }, { "22/08/2022": "Juntada de Documento Nº Protocolo: WTRJ.22.70028500-0 Tipo da Petição: Petição Data: 22/08/2022 16:12" }, { "22/08/2022": "Juntada de Petição de Nº Protocolo: WTRJ.22.70028500-0 Tipo da Petição: Petição Data: 22/08/2022 16:12" }, { "06/06/2022": "Enviado para análise do Juízo de Admissibilidade RESP/RE" }, { "03/06/2022": "Juntada de Petição de Nº Protocolo: WTRJ.22.70018679-6 Tipo da Petição: Contrarrazões Data: 03/06/2022 15:26" }, { "01/06/2022": "Concluso à Vice - Presidência" }, { "31/05/2022": "Certidão Emitida CONCLUSÃO Faço estes autos conclusos ao Excelentíssimo Senhor Des. José Carlos Malta Marques, Vice - Presidente. Maceió, 30 de maio de 2022 Adriana Mota Alcides Chefe de Gabinete da Vice-Presidência" }, { "30/05/2022": "Interposto Recurso Especial" }, { "30/05/2022": "Realizada Alteração de Relatoria Orgão Julgador Anterior: 2ª Câmara Cível Orgão Julgador Novo: Vice-Presidência Relator Anterior: Des. Otávio Leão Praxedes Relator Novo: Des. José Carlos Malta Marques Motivo da alteração: recurso especial" }, { "30/05/2022": "Processo Redistribuído Antigo órgão julgador: 2ª Câmara Cível Antigo relator: Des. Otávio Leão Praxedes" }, { "27/05/2022": "Encaminhado para secretaria da Vice-Presidência" }, { "27/05/2022": "Certidão Emitida Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Otávio Leão Praxedes Apelante : Cony Engenharia Ltda.. Advogado : Carlos Henrique de Mendonça Brandão (6770/AL). Advogada : Maria Eugênia Barreiros de Mello (14717/AL). Advogado : Vítor Reis de Araujo Carvalho (14928/AL). Advogado : Guilherme Freire Furtado (14781/AL). Apelante : Banco do Brasil S A. Advogado : Nelson Wilians Fratoni Rodrigues (9395A/AL). Apelado : José Carlos Cerqueira Souza Filho. Advogado : Vinicius Faria de Cerqueira (9008/AL). Apelada : Livia Nascimento da Rocha. Advogado : Vinicius Faria de Cerqueira (9008/AL) CERTIDÃO DE JUNTADA E REMESSA À SECRETARIA DA VICE-PRESIDÊNCIA Certifico, para os devidos fins, a juntada, nos presentes autos, do(s) incidente(s) de n.º : 0710802-55.2018.8.02.0001/50000 às páginas 776/806. Certifico, ainda, que decorreu o prazo legal sem que as demais partes interpusessem quaisquer incidentes e/ou recursos pertinentes à(o) Decisão/Acórdão retro. Certifico por último que faço remessa, nesta data, à Secretaria da Vice-Presidência, pois a(s) parte(s) Cony Engenharia Ltda. interpôs/interpuseram Recurso Especial às páginas 760/771. O referido é verdade e dou fé. Maceió, 27 de maio de 2022. Carla Christini Barros Costa de Oliveira Secretário(a) da 2ª Câmara Cível Luiz Carlos Maciel Rodrigues Analista Judiciário" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Juntada de Documento" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Juntada de Documento" }, { "27/05/2022": "Juntada de Petição de" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Juntada de Petição de" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Juntada de Documento" }, { "27/05/2022": "Certidão Emitida" }, { "27/05/2022": "Juntada de Petição de" }, { "27/05/2022": "Certidão Emitida Apelação Cível nº 0710802-55.2018.8.02.0001 Relator :Des. Otávio Leão Praxedes Apelante: Cony Engenharia Ltda.. Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL). Advogada: Maria Eugênia Barreiros de Mello (OAB: 14717/AL). Advogado: Vítor Reis de Araujo Carvalho (OAB: 14928/AL). Advogado: Guilherme Freire Furtado (OAB: 14781/AL). Apelante: Banco do Brasil S A. Advogado: Nelson Wilians Fratoni Rodrigues (OAB: 9395A/AL). Apelado: José Carlos Cerqueira Souza Filho. Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL). Apelada: Livia Nascimento da Rocha. Advogado: Vinicius Faria de Cerqueira (OAB: 9008/AL). CERTIDÃO DE JUNTADA Junto, nesta data, aos presentes autos, os documentos pertinentes ao(s) Incidente(s) n.º 0710802-55.2018.8.02.0001/50000. Maceió,27 de maio de 2022. Carla Christini Barros Costa de Oliveira 2ª Câmara Cível Luiz Carlos Maciel Rodrigues Analista Judiciário" }, { "25/05/2022": "Juntada de Documento Nº Protocolo: WTRJ.22.70016995-6 Tipo da Petição: Recurso Especial Cível Data: 25/05/2022 10:47" }, { "25/05/2022": "Juntada de Documento Nº Protocolo: WTRJ.22.70016995-6 Tipo da Petição: Recurso Especial Cível Data: 25/05/2022 10:47" }, { "25/05/2022": "Juntada de Documento Nº Protocolo: WTRJ.22.70016995-6 Tipo da Petição: Recurso Especial Cível Data: 25/05/2022 10:47" }, { "25/05/2022": "Juntada de Petição de Nº Protocolo: WTRJ.22.70016995-6 Tipo da Petição: Recurso Especial Cível Data: 25/05/2022 10:47" }, { "22/10/2021": "Juntada de Petição de Protocolo nº WTRJ.2170030289-2 Embargos de Declaração Cível" }, { "22/10/2021": "Incidente Cadastrado Seq.: 50 - Embargos de Declaração Cível" }, { "13/10/2021": "Publicado" }, { "13/10/2021": "Certidão Emitida Apelação Cível nº 0710802-55.2018.8.02.0001 Relator: Des. Otávio Leão Praxedes Apelante: Cony Engenharia Ltda.Advogado: Carlos Henrique de Mendonça Brandão (OAB: 6770/AL)Advogada: Maria Eugênia Barreiros de Mello (OAB: 14717/AL)Advogado: Vítor Reis de Araujo Carvalho (OAB: 14928/AL)Advogado: Guilherme Freire Furtado (OAB: 14781/AL)Apelante: Banco do Brasil S AAdvogado: Nelson Wilians Fratoni Rodrigues (OAB: 9395A/AL)Apelado: José Carlos Cerqueira Souza FilhoAdvogado: Vinicius Faria de Cerqueira (OAB: 9008/AL)Apelada: Livia Nascimento da RochaAdvogado: Vinicius Faria de Cerqueira (OAB: 9008/AL) CERTIDÃO DE DISPONIBILIZAÇÃO DO ACÓRDÃO CERTIFICO, que foi disponibilizado no Diário da Justiça Eletrônico do Tribunal de Justiça de Alagoas em 13/10/2021 e considerado publicado em 14/10/2021 a conclusão do venerando Acórdão julgado em 07/10/2021, nos termos do Artigo 943, § 2º do Código de Processo Civil c/c o artigo 4º, § 3º, da Lei nº 11.419/2006. Maceió/AL, 13 de outubro de 2021 Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível Gabrielle Wanderley Tenório Cavalcante Analista Judiciário" }, { "07/10/2021": "Conhecido o recurso de Vistos, relatados e discutidos estes autos do Recurso de Apelação Cível nº 0710802-55.2018.8.02.0001, em que figuram, como parte apelante, Cony Engenharia LTDA e Banco do Brasil S/A; e, como parte apelada, José Carlos Cerqueira Souza Filho e Livia Nascimento da Rocha, ACORDAM, os Desembargadores integrantes desta 2ª Câmara Cível do Tribunal de Justiça do Estado de Alagoas, à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. Participaram do julgamento os eminentes Desembargadores constantes na Certidão de Julgamento." }, { "07/10/2021": "Certidão Emitida Certifico que a 2ª Câmara Cível, assim decidiu: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator.. Participaram do julgamento: Juiz Conv. Carlos Cavalcanti de Albuquerque Filho, Des. João Luiz Azevedo Lessa, concovado em face das férias da Desa. Elisabeth Carvalho Nascimento e Des. Otávio Leão Praxedes. Presidiu a sessão o Exmo. Senhor Des. Otávio Leão Praxedes. Para constar lavro a presente certidão, do que dou fé. Maceió, 07 de outubro de 2021. Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível" }, { "07/10/2021": "Processo Julgado à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator." }, { "27/09/2021": "Certidão Emitida CERTIDÃO Certifico que o presente processo foi incluído na pauta de julgamento do dia 07 de outubro de 2021 às 9:00h, disponibilizado no Diário de Justiça Eletrônico no dia 27 de setembro de 2021, nos termos dos art. 6º da Resolução n.º 318/20 do CNJ, tendo sido a mesma afixada no mural informativo jurisdicional desta Corte de Justiça. Obs.: Em cumprimento a Resolução n. 13/2020, e ao art 1º do Ato Normativo n. 13/2021 disponibilizado no Diário de Justiça Eletrônico em 07/07/2021, as inscrições para sustentações orais deverão ser feitas EXCLUSIVAMENTE pelo sítio do Tribunal de Justiça (http://sadv.tjal.jus.br/login). Em caso de adiamento do julgamento, o advogado terá que realizar nova inscrição e credenciamento pelo portal. Maceió, 27 de setembro de 2021 Carla Christini Barros Costa de Oliveira Secretária da 2ª Câmara Cível" }, { "24/09/2021": "Inclusão em pauta Para 07/10/2021" }, { "23/09/2021": "Publicado" }, { "22/09/2021": "Solicitação de dia para Julgamento - Relator DESPACHO Trata-se de dois Recursos de Apelação Cível, o primeiro interposto pelo Banco do Brasil S/A, às págs. 668/689, e o segundo interposto pela Cony Engenharia LTDA, às págs. 693/701, ambos em face da Sentença proferida pelo Juízo de Direito da 4ª Vara Cível da Capital, às págs. 649/663, que julgou parcialmente procedentes os pedidos da Ação Declaratória de Nulidade de Contrato de Financiamento Bancário c/c Indenização por Danos Materiais e Morais proposta por , às págs. 1/30, conforme se pode verificar no dispositivo abaixo transcrito: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a datada efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em danos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como corolário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se. (págs. 661/663 - Sem grifos no original). Em suas razões recursais, o Banco do Brasil S/A aduziu que: i) preliminarmente, é parte ilegítima para figurar no polo passivo da ação de origem, pois é mero agente financeiro e os descontos decorrentes do financiamento só iniciam após o \"habite-se\"; ii) a taxa de evolução de obra, também chamada de juros de obra, é cobrada nos financiamentos na modalidade créditos associativos para aquisição de imóveis na planta, mas o apelante não realiza esse tipo de cobrança, ele cobra apenas encargos adicionais, que correspondem aos juros devidos, tanto no período em que o imóvel ainda está na planta, quanto após o início do pagamento da parcela de amortização de capital; iii) a cobrança da referida taxa só se inicia após o \"habite-se\"; iii) o apelante não tem como acompanhar a evolução das milhares de obra que financia, cabendo à construtora comprovar que o \"habite-se\" foi liberado pela Prefeitura; iv) caso a apelada tivesse levado a cópia do \"habite-se\" à instituição financeira, o encargo já não seria mais cobrado; v) deve-se respeitar o princípio do pacta sunt servanda, pois o apelante apenas cumpriu o que foi determinado em contrato; vi) inexiste dever de indenizar, ante a ausência da prática de ato ilícito; e, vii) em caso de condenação ao pagamento de indenização por danos morais, o valor arbitrado não pode ensejar enriquecimento ilícito. Ao final, requereu o conhecimento e o provimento do presente Recurso de Apelação Cível, a fim de reformar a Sentença proferida pelo Juízo de Direito de Primeiro Grau, no sentido de julgar improcedentes os pedidos autorais; e, subsidiariamente, reduzir o valor arbitrado a título de indenização por danos morais. Por sua vez, a Cony Engenharia LTDA alegou que: i) a parte apelada sustenta que houve atraso na entrega de uma unidade imobiliária do empreendimento Dellavia Park Club; ii) o Juízo a quo entendeu que o atraso na entrega do imóvel seria incontroverso, o que necessariamente implicaria que a parte apelada teria deixado de auferir lucros a título de alugueis no período; iii) a presunção adotada pelo Juízo a quo de que o atraso na entrega do imóvel implica danos materiais, mais especificamente na modalidade de lucros cessantes, não é absoluta; iv) na petição inicial, a parte apelada afirma que o imóvel foi adquirido para sua própria moradia, de modo que nunca houve intenção de locação nem de auferir renda com o bem; v) as provas dos autos não deixam dúvidas sobre a finalidade de moradia da parte apelada e, por consequência, os supostos danos são meramente hipotéticos e sem correspondência com a realidade dos fatos; vi) o contrato de promessa de compra e venda foi celebrado unicamente pelo Sr. José Carlos Cerqueira, de modo que não há que se falar em danos morais à Sra. Livia Nascimento, já que não figurou como parte contratante com a empresa; vii) em relação aos supostos danos morais causados ao Sr. José Carlos Cerqueira, não houve violação a qualquer direito da personalidade; e vii) é válida a cláusula de tolerância de dezoito meses pactuada entre as partes e a aplicabilidade do INCC à correção do saldo devedor, não devendo prevalecer o entendimento do Juízo a quo pelo limite de tolerância de apenas cento e oitenta dias nem a substituição do índice pelo IGP-M para correção do saldo devedor. Por derradeiro, requereu o conhecimento e o provimento do presente Recurso de Apelação Cível, a fim de reformar a Sentença proferida pelo Juízo de Direito de Primeiro Grau, no sentido de julgar improcedentes os pedidos autorais; e, subsidiariamente, adotar a data de agosto de 2018 como referência para eventuais cálculos devidos e manter o INCC para correção do saldo devedor. Intimada a apresentar contrarrazões, a parte apelada alegou que: i) a preliminar de ilegitimidade passiva do Banco do Brasil S/A não merece prosperar, pois a presente lide diz respeito a negócios jurídicos diretamente ligados à instituição financeira, como a abusividade do contrato de financiamento, nulidade de cláusulas de financiamento e devolução das taxas de obra ilegalmente cobradas; a construtora não alegou em momento oportuno a preliminar de ilegitimidade passiva da Sra. Lívia Nascimento, sendo irrelevante qualquer argumento nesse sentido em sede recursal, por mais que o dano tenha sido evidenciado em razão da privação do bem sofrida juntamente com seu marido por tempo além do razoável; ii) a construtora só poderia fazer prova de que a mora contratual não lhe é imputável, mas não o fez; iii) os anos de espera e de expectativas, de frustrações, de chateações, de descontentamentos, discussões, mentiras e novas frustrações são suficientes para comprovar o dano moral; iv) a cláusula de tolerância de dezoito meses prevista no contrato afronta a jurisprudência do Superior Tribunal de Justiça, que já limitou o prazo de cento e oitenta dias; e v) o inadimplemento dos réus, em razão do atraso na entrega do imóvel, não pode gerar acréscimo ao saldo devedor, sob pena de onerar indevidamente o consumidor, pois transferiria os encargos da mora a quem não deu causa e mais, remunerando a construtora/incorporadora pelo próprio inadimplemento. Por fim, requereu o não provimento do Recurso de Apelação Cível, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau, apenas majorando os honorários advocatícios sucumbenciais. É, em síntese, o relatório. Estando o processo em ordem, peço inclusão na pauta de julgamento subsequente. Maceió, 22 de setembro de 2021 Des. Otávio Leão Praxedes Relator" }, { "22/07/2021": "Juntada de Petição de Nº Protocolo: WTRJ.21.70018896-8 Tipo da Petição: Petição Data: 22/07/2021 16:32" }, { "25/05/2021": "Juntada de Petição de Nº Protocolo: WTRJ.21.70013501-5 Tipo da Petição: Petição Cível Data: 25/05/2021 10:29" }, { "22/02/2021": "Concluso ao Relator" }, { "22/02/2021": "Termo de Distribuição Emitido" }, { "22/02/2021": "Processo Distribuído por Sorteio Órgão Julgador: 2 - 2ª Câmara Cível Relator: 86 - Des. Otávio Leão Praxedes" }, { "22/02/2021": "Processo Cadastrado" }, { "22/02/2021": "Recebidos os Autos pela Entrada de Recursos Foro de origem: Foro de Maceió Vara de origem: 4ª Vara Cível da Capital" } ]

    assert result == expected