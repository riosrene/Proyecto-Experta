# Proyecto-Experta

Para la evaluacion tecnica de la pagina experta.com.ar, se eligio automatizar 2 funcionalidades y para ello se utilizo los siguientes componentes:

Laptop:
 - AMD E2-1800 APU with Radeon(tm) HD Graphics   1.70 GHz 
 - Windows 10 Pro 64 Bits
 - Python Ver. 3.8
 - PyCharm Ver. Community 2020.1
 - Navegador Google Chrome Versión 84.0.4147.105 (Build oficial) (64 bits).
 
Las 2 funcionalidades que se eligieron para automatizar se encuentran en el menu principal opcion SEGUROS/PERSONAS, sub opcion ACCIDENTES PERSONALES y HOGAR, en cada opcion se automatizo en Lenguaje Python y la pruebas en Unittest. En cada opcion se localizaron elementos que permitio realizar las pruebas. Estas opciones se escogieron por ser medulares al negocio.

Los archivos de dichas pruebas en Python son, main_test_acciper.py opcion principal SEGUROS/PERSONAS ACCIDENTES PERSONALES y main_test_hogar.py opcion principal SEGUROS/PERSONAS HOGAR.
 
 
Preguntas:

1) Explicar el Page Object Model u otro patrón de diseño que sepa.
El Page Object Model es un patrón de diseño de objetos en Selenium, donde cada página web, se representan como una clase y los elementos de la página se define como variables de clases, el Page Object encapsula el comportamiento de las paginas, o una parte de ella, con una API especifica de la aplicación, lo cual permite realizar test y manipular los elementos de pagina sin tener que lidiar con el HTML, el Page Object Model se utilizar para realizar pruebas funcionales automatizadas.

2) Cómo decide cuándo automatizar un test? En qué casos no automatizaría un test?
Lo primero que se debe hacer es una evaluación de lo que necesitan automatizar, por lo general funcionalidades que llevan mucho tiempo para ser realizadas en pruebas manuales, repetitivas, regresiones las cuales tengan sentido la automatización, algo que se utilizara. Todo esto debe ser evaluado en conjunto con el team Manual y el Team de automatización porque se debe determinar si es factible a nivel técnico. (Si hay alguna limitación y es posible no automatizar), además, deben ser sistemas que no tengan demasiadas modificaciones y deben ser estables y prácticamente sin errores lo cual haría difícil la automatización ya que tendrían mas cambios y habría que volver hacerlo todo de nuevo. Es necesario que los sistemas esten estables para validar que los sistemas estén activos y funcionando, como precondición el sistema no debería tener errores, pero luego que se automatice puede ser que presenten errores de ahí la importancia de las regresiones. 
En que casos no automatizaría, cuando por ejemplo tengo limitaciones de tecnología, es decir, que no se pueda realizar por algo técnico o que no sea estable el ambiente.

3) Conoce Docker?
Si, Docker es una herramienta (Proyecto de Código abierto) que automatiza el despliegue de aplicaciones dentro de contenedores de software. 

4) Conoce Selenium Hub?
He leído al respecto, mas no lo he utilizado.

5) En la última empresa en la que trabajabas/trabajas:
a) En que momento se testeaba?
Una vez obtenido de parte del Analista Funcional los requerimientos del sistema y en reunión con el equipo de desarrollo si iniciaba los diseños de casos de pruebas y en lo que se refiere a realizar test en automation pues se realiza una    reunión con el QA manual y el de automation para evaluar la factibilidad a nivel técnico.

b)	En que tipo de reuniones participabas? Si de las plannings se trata, que aportabas a la reunión?
Participaba en las Reuniones Diarias (DaIly Scrum) y en las que el líder reunía al equipo para dar información sobre el desarrollo y avance del proyecto. En las reuniones mi aporte consistía en dar ayuda, colaborar, ser proactivo y aportar ideas que permitan que el proyecto continúe con lo planificado junto al equipo que lo compone.
   
