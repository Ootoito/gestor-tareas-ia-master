# PRAKTIKO – DOCUMENTO MAESTRO DE ARQUITECTURA Y DESARROLLO

**Versión:** 1.0
**Fecha:** Julio 2026

## Objetivo

Este documento sirve como contexto maestro para continuar el desarrollo de Praktiko en un chat nuevo sin depender del historial de conversaciones.

# 1. Filosofía del proyecto

Praktiko evoluciona hacia un asistente inteligente de aprendizaje de idiomas. La IA debe actuar como profesor y entrenador personal utilizando únicamente datos reales calculados por la aplicación.

# 2. Arquitectura

- Vistas modularizadas por área funcional.
- Lógica de negocio en servicios.
- IA centralizada en `praktiko/servicios/ia_service.py`.
- Reutilizar código antes de crear nuevas implementaciones.

# 3. Estado del despliegue

Documentar siempre:
- VPS
- Dominio
- systemd
- Entorno virtual
- Git
- Ramas
- Estructura de despliegue

# 4. Internacionalización

Todo HTML nuevo debe salir internacionalizado.

Idiomas:
- Español
- Inglés
- Ruso
- Esperanto

# 5. Responsive

Toda funcionalidad nueva debe funcionar en escritorio y móvil.

# 6. Filosofía de desarrollo

- Modularizar vistas.
- Separar servicios.
- No duplicar consultas.
- No duplicar lógica.
- Revisar primero el código existente.

# 7. Base de datos

Motor: MariaDB

Conceptualmente:
- Usuarios
- Diccionarios
- Temas
- Entradas
- Estadísticas
- Historial
- Grupos
- Invitaciones

# 8. Estado funcional

- Usuarios ✅
- Diccionarios ✅
- Juego normal ✅
- Mahjong ✅
- Grupos ✅
- Estadísticas ✅
- Palabras difíciles ✅
- Asistente IA 🟡
- Profesor IA ⏳
- Planes IA ⏳

# 9. IA

Toda la IA se centraliza en el Asistente IA.

Principios:
- No inventar datos.
- Interpretar únicamente datos reales.
- Devolver acciones estructuradas.
- Reutilizar la integración OpenAI existente.

# 10. OpenAI

Variables:
- OPENAI_API_KEY
- OPENAI_MODEL

Utilizar Responses API ya existente.

# 11. Estado actual

La recomendación IA ya utiliza OpenAI.
El siguiente paso es enriquecer el prompt con más datos reales del usuario.

# 12. Roadmap

- Mejorar prompt.
- Profesor IA.
- Generación de ejercicios.
- Planes de estudio.
- IA para grupos.

# 13. Reglas de colaboración

Siempre indicar:
- Fichero.
- Localizar bloque.
- Añadir después de...
- Sustituir por...

Entregar fichero completo cuando el cambio sea importante.

# 14. ADR

- Vistas modularizadas.
- Servicios independientes.
- IA en Asistente IA.
- IA devuelve acciones.
- HTML internacionalizado.
- Responsive obligatorio.

# 15. No volver a proponer

- Crecer views.py.
- Otra integración OpenAI.
- Botones IA fuera del Asistente IA.
- HTML sin gettext.
- Duplicar lógica.

# 16. Riesgos técnicos

- Crecimiento de vistas.
- Duplicación de lógica.
- Pérdida de responsive.
- Romper internacionalización.
- Divergencia local/VPS.

# 17. Principios de calidad

- Reutilizar código.
- Documentar consultas complejas.
- Mantener compatibilidad.
- Revisar el código antes de desarrollar.

# 18. Próxima sesión

1. Revisar el prompt.
2. Enriquecer contexto.
3. Añadir nuevas acciones IA.
4. Evolucionar el entrenador personal.

