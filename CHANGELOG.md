# CHANGELOG

## [0.5.0-dev] - 11/07/2022

### Added

* **Models**:
    * CMS - Base models.
    * CMS - Home models.
    * CMS - About models.
    * CMS - Project models.
    * CMS - Technology models.
    * Contact records models.
    * Support for SVG files in logo fields.
    * Support for auto-generate webp images from image fields in order to optimize the website.
    * ImageValidator, ExtensionValidator and MaxFileSizeValidator to file-based fields.
    * Register models in Django Admin to allow customizations.
    * Preview of image fields in Django Admin.

* **Forms**:
    * Contact form.

* **Views**:
    * Home, About, Projects and Contact views.

* **Templates**:
    * Information modal on Home Page.
    * Title and technologies to each project card on Projects Page.
    * Linked CMS models to templates.
    * Tailwind typography to Project Detail to allow WYSIWYG styles.

### Changed

* **Templates**:
    * Navbar background color on scroll down to improve the visibility.

* **Models**:
    * Change WYSIWYG editor from Ckeditor to TinyMCE.

## [0.3.0-dev] - 23/06/2022

### Added

* **Templates**:
    - About page template
    - Projects page template
    - Project detail page template
    - Contact page template

## [0.2.0-dev] - 20/06/2022

### Added

* **Packages**:
    - Flowbite to tailwind.config.js
    - Fontawesome from pypi
* **Templates**:
    - Base template
    - Home page template

## [0.1.0-dev] - 18/06/2022

### Start Project: Basic config + Tailwind

#### Follow the README file to run the project in development mode.

- Start project
- Added requirements
- Config tailwind and browser-reload.
- Config basic url patterns, the "website" app and initial templates (**base.html**, errors **[400|403|404|500].html**).


