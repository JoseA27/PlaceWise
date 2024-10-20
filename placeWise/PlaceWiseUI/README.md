# PlaceWise UI

## Descripción

Este repositorio contiene el frontend de la aplicación PlaceWise UI, desarrollada en React y estructurada según Atomic Design Pattern, con Tailwind CSS para estilos.

## Estructura de Carpetas

- **assets**: Contiene archivos estáticos como imágenes.
- **components**: Componentes React organizados en `atoms`, `molecules`, `organisms`, y `templates`.
- **pages**: Páginas de la aplicación, cada una representando una vista única.
- **styles**: Configuración y estilos de Tailwind CSS.
- **utils**: Funciones de utilidad que son usadas en toda la aplicación.

```
PlaceWiseUI/
├── assets/
│   └── logo.png
├── components/
│   ├── atoms/
│   │   ├── CancelButton.jsx
│   │   ├── Dropzone.jsx
│   │   ├── InputField.jsx
│   │   ├── Logo.jsx
│   │   ├── SaveButton.jsx
│   │   ├── SelectField.jsx
│   │   ├── SocialIcon.jsx
│   │   ├── TextAreaField.jsx
│   │   ├── UploadIcon.jsx
│   │   ├── UploadInstructions.jsx
│   │   └── UploadMediaButton.jsx
│   ├── molecules/
│   │   ├── CreatePropertyForm.jsx
│   │   ├── DocumentUpload.jsx
│   │   ├── FileUpload.jsx
│   │   ├── ImageUpload.jsx
│   │   ├── NavLinks.jsx
│   │   ├── SearchBar.jsx
│   │   ├── SocialIcons.jsx
│   │   ├── UserMenu.jsx
│   │   └── VideoUpload.jsx
│   ├── organisms/
│   │   └── Header.jsx
│   ├── pages/
│   │   ├── UploadMediaPage.jsx
│   │   └── UploadPropertyPage.jsx
│   └── templates/
│       ├── FileUploadTemplate.jsx
│       ├── MainLayout.jsx
│       └── PropertyFormTemplate.jsx
├── auth/
│   ├── AuthContext.jsx
│   ├── useAuth.js
│   └── PrivateRoute.jsx
├── hooks/
│   ├── useForm.js
│   └── useMediaUpload.js
├── context/
│   └── GlobalContext.jsx
├── styles/
│   └── tailwind.css
├── utils/
│   ├── helpers.js
│   └── validators.js
├── .gitignore
├── package-lock.json
├── package.json
├── tailwind.config.js
└── README.md
```

### Descripción de los Archivos 

#### assets/: 
Contiene recursos estáticos, como el logotipo del proyecto (logo.png).

#### **components/**: 
Almacena todos los componentes React, organizados en subcarpetas:

- **Atoms/**: Componentes básicos e independientes, como botones, íconos y campos de entrada.
    - **CancelButton.jsx**: Componente de botón para cancelar acciones.
    - **Dropzone.jsx**: Área de arrastre para carga de archivos.
    - **InputField.jsx**: Componente para campos de entrada.
    - **Logo.jsx**: Componente de logo, que puede incluir el logotipo del proyecto.
    - **SaveButton.jsx**: Botón para guardar cambios.
    - **SelectField.jsx**: Campo de selección para opciones desplegables.
    - **SocialIcon.jsx**: Ícono para enlaces de redes sociales.
    - **TextAreaField.jsx**: Componente para áreas de texto.
    - **UploadIcon.jsx**:  Ícono para el botón de subida de archivos.
    - **UploadInstructions.jsx**: Componente de instrucciones para la carga de archivos.
    - **UploadMediaButton.jsx**: Botón para abrir la pantalla de carga de medios.
- **molecules/**: Componentes compuestos por átomos, como formularios y menús.
    - **CreatePropertyForm.jsx**: Formulario principal para ingresar los detalles de la propiedad.
    - **DocumentUpload.jsx**: Componente para la carga de documentos.
    - **FileUpload.jsx**: Componente general de carga de archivos.
    - **ImageUpload.jsx**: Componente para la carga de imágenes.
    - **NavLinks.jsx**: Enlaces de navegación para el menú principal.
    - **SearchBar.jsx**: Barra de búsqueda.
    - **SocialIcons.jsx**: Íconos de redes sociales agrupados.
    - **UserMenu.jsx**: Menú para el perfil de usuario.
    - **VideoUpload.jsx**: Componente para la carga de videos.
- **organisms/**: Componentes más complejos que combinan moléculas y átomos.
    - **Header.jsx**: Contiene el encabezado de la aplicación con logo, menú de usuario y enlaces de navegación.

- **templates/**: Plantillas para organizar el diseño general de las páginas.
    - **FileUploadTemplate.jsx**: Plantilla para manejar la carga de diferentes tipos de archivos.
    - **MainLayout.jsx**: Estructura general de la aplicación, que incluye el encabezado y el diseño base.
    - **PropertyFormTemplate.jsx**: Plantilla del formulario principal de propiedad.

- **pages/**: Contiene las vistas principales del proyecto, como las páginas para cargar propiedades y medios.
    - **UploadMediaPage.jsx**: Página para agregar media a la propiedad.
    - **UploadPropertyPage.jsx**: Página principal para la creación de propiedades.

#### **auth/**:
Módulos relacionados con la autenticación de usuarios.

- **AuthContext.jsx**: Proveedor de contexto de autenticación.
- **useAuth.js**: Hook personalizado para manejar la autenticación de usuarios.
- **PrivateRoute.jsx**: Componente para proteger rutas que requieren autenticación.

#### **hooks/**:
Contiene hooks personalizados para simplificar la lógica reutilizable.

- **useForm.js**: Hook personalizado para manejar la lógica de formularios.
- **useMediaUpload.js**: Hook para gestionar la subida de archivos multimedia.

#### **context/**:
Proveedores de contexto que permiten el manejo del estado global de la aplicación.

- **GlobalContext.jsx**: Proveedor del contexto global para compartir el estado entre múltiples componentes.

#### **styles/**: 
Incluye configuraciones y estilos globales, en este caso con Tailwind CSS.

- **tailwind.css**: Estilos base configurados con Tailwind CSS.

#### **utils/**: 
Funciones auxiliares y de utilidad.

- **helpers.js**: Funciones auxiliares como formateadores de fechas y otros utilitarios.
- **validators.js**: Funciones para validar entradas de usuario en formularios.

#### **.gitignore**: 
Archivo de configuración para ignorar carpetas innecesarias en Git, como node_modules.

#### **package-lock.json**: 
Congela las versiones exactas de las dependencias para asegurar consistencia, optimiza la instalación y garantiza la integridad de los paquetes.

#### **package.json**: 
Define las dependencias del proyecto, scripts y configuración de la aplicación.

#### **tailwind.config.js**: 
Configuración de Tailwind CSS para personalizar los estilos.

#### **README.md**: 
Documentación del proyecto, incluyendo estructura de carpetas, y descripción de los componentes.