**_Nota Propia:_** Las funciones que se dejaron de tarea se hicieron a prueba y error testeandolas a lo largo de código y si no daba un resultado bueno, se volvía a modificar la función y repetir el proceso hasta que los resultados presentarán un error por debajo de $$10^{-6}$$.

[Link problemas de álgebra](https://drive.google.com/drive/folders/1cxqYcDHZe2e2QsGAepYZ9G59IrIf49kq)

**TENGO PROBLEMAS CON EL ESCANER PERO SUBIRÉ FOTOS DE MANERA PROVICIONAL EN LO QUE RESUELVO EL PROBLEMA PORQUE ME PIDE INSTALAR EL SOFTWARE DE NUEVO.**

[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2864937&assignment_repo_type=AssignmentRepo)
# practica-semanal-2-2020
 Segunda práctica semanal del prope-2020 

La entrega es para el domingo **21 de junio 11:59 pm**.

1) Resolver ejercicios que dicen **Tarea** de [1_aproximacion_a_derivadas_e_integrales](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/2_calculo_DeI/1_aproximacion_a_derivadas_e_integrales.ipynb)

Los módulos pedidos deben colocarlos en la raíz de su repo (no colocarlos dentro de directorios).

Adicionalmente deben crear *milestones* e *issues* para que organicen su trabajo vía github. Por ejemplo:

*Milestone* "Resolver ejercicios de diferenciación numérica en nota". Tal *milestone* tendrá los *issues*:

* *Issue1*: leer nota y entender definiciones.
* *Issue2*: en jupyterlab ir resolviendo de manera interactiva el ejercicio1 de **Tarea**.
* *Issue3*: en jupyterlab ir resolviendo de manera interactiva el ejercicio2 de **Tarea** para crear el módulo `diferenciacion_centrada.py` y subirlo al repo.

...

y en sus commits harían referencia a los issues conforme van realizando su trabajo, por ejemplo:

```
git commit -m "finalizando la lectura de nota de acuerdo al issue #1" -i <archivo que resuelve issue1>
```

Una vez que terminen el issue ciérrenlo.

Este punto número 1) se auto calificará con github Actions, ver [actions](https://github.com/features/actions) para info sobre este feature de github. Para que funcione esto primero deben revisar que en la tab de Actions:

<img src="https://dl.dropboxusercontent.com/s/kb7ctrv8alqgrs5/actions_gh.png?dl=0" heigth="800" width="800">

tienen activo el "Github Actions Workflow":

<img src="https://dl.dropboxusercontent.com/s/l5bea3adsjyn0yk/actions_gh_2.png?dl=0" heigth="800" width="800">


Si no lo tienen activo avisar al prof. Si lo tienen activo trabajen como normalmente lo realizan subiendo archivos a github.

2) Resolver los ejercicios de [3_algebra_lineal/0_definiciones_generales](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/0_definiciones_generales.ipynb). 

* Si eligieron la opción de realizar los ejercicios en papel, colocar una liga en el `README.md` de la raíz de su repo de gh-classroom que dirija a un servicio externo de almacenamiento (por ejemplo google drive, dropbox,...) con los ejercicios realizados.

* Si eligieron la opción de realizar los ejercicios en *notebooks* de jupyterlab, subir tales notebooks al repo de gh-classroom.


Aquí el botón de *binder* que ayuda para quienes no tienen instalado de forma local jupyterlab:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/palmoreck/dockerfiles-for-binder/jupyterlab_prope_r_kernel_tidyerse?urlpath=lab/tree/Propedeutico)

**Recuerden:**

* Ir guardando su trabajo si usan *binder*.

* Usar git o github para añadir archivos a sus repos de gh-classroom. Algunos comandos de git útiles para añadir un archivo (por ejemplo un notebook) son:

```
git clone <url de mi repo que está en gh-classroom> <aquí colocar nombre de un directorio>

#el comando anterior les pedirá sus credenciales de github tecleen la respuesta y den enter por cada respuesta

cd <nombre del directorio elegido en la línea anterior> #cd es "change directory" y lo usamos para entrar al directorio

```

```
git config --global user.email "<mi correo asociado de github>"
git config --global user.name "<mi nombre>"
git add <nombre de mi notebook>
git commit -m "mensaje de mi commit" -i <nombre de mi notebook>
git push origin master
```

La última línea les pedirá sus credenciales de github.

Después de realizar por primera vez lo anterior si quiero hacer cambios en mi notebook el flujo que sigo es:

```
#clonar repo a un directorio si no lo tengo clonado
#entrar al directorio con cd
#git config --global user.email "<mi correo asociado de github>"
#git config --global user.name "<mi nombre>"
git commit -m "mensaje de mi commit con los cambios" -i <nombre de mi notebook>
git push origin master
```

La última línea les pedirá sus credenciales de github.
