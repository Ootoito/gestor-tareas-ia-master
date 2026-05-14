-- ===============================================
-- Migración de tareas.txt a PostgreSQL
-- ===============================================
BEGIN;

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y acualizar la hoja de seguimiento expediente 38-CREM21-0082-038 | CREAR EXPEDIENTE DE REINTEGRO',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 38-CREM22-0069-020',
    'Informe en ruta \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana\51. 43782442X DOMINGO FARIÑA MARTIN (38-CREM22-0069-020) REVISADO | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022Nombre: | resolucion_justificacion_38-CREM22-0069-020 | pdf.: | resolucion_justificacion_38-CREM22-0069-020',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar la visita (ver email)',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\José Ramón\Notificacion Visitas',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Urgente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just parcial tras requerimiento del expte 35-CREM21-0064-026',
    'Ejemplo RESOL_JUST_PARCIAL_TRAS_REQUERIMIENTO_2021_Miriam_Sanchez en ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Doc.Trabajo | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Doc.Trabajo | Documento: | RESOL_JUST_PARCIAL_TRAS_REQUERIMIENTO_2021_BORJA CRUZ VELAZQUEZ | Revisar por que tiene un anexo en la última pagina. | El informe técnico tiene un error de un céntimo en el importe de la devolución, ya corregido en el texto de la resolución, | Ruta informe técnico: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER | Nombre: | INFORME TECNICO DE JUSTIF PARCIAL BORJA CRUZ VELAZQUEZ firmado',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y acualizar la hoja de seguimiento. CREAR EXPEDIENTE DE REINTEGRO. 38-CREM21-0049-011).',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y acualizar la hoja de seguimiento. CREAR EXPEDIENTE DE REINTEGRO. 35-CREM21-0021-027',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y acualizar la hoja de seguimiento',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total | 38-CREM22-0005-006',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic (OJO JUSTIFICACIÓN) | CREAR expediente de reintegro',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021 | 35-CREM21-0090-014',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 38-CREM22-0005-006',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana\26. 43376975X M. INES GUTIERREZ TOLEDO (38-CREM22-0005-006) REVISADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/12/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'PREPARAR RESOLUCIONES 2022',
    'Cuadro 2022, todas las verdes. | -Combinada preparar modelo ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total | - datos combinados preparar ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total | - Informes en cada uno en su carpeta | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana | - Resoluciones de abono: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total | Es única comprobar que estén en anexo I',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('27/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar la doc de hiperreg de contestación a los requerimientos',
    'esto le gusta a Diana / VAMOS A VER PRUEBA DE FILTRADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('25/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Programada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Gestionar expedientes de AA de Las Palmas (SICOIN)',
    'Enviado correo a Fernando el 25-11-2025',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('25/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Programada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear los SUDEV del expediente | 38-CREM22-0019-023',
    'Pte de hacer modelo de resolución.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Cuadro notificaciones requerimiento 2019 y 2021',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\José Ramón | Nombre: | notificaciones acceso sede',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y publicar en el tablón de anuncios el requerimiento de justificación de 2021',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, actualizar hoja de seguimiento y cerrar seflogic de expediente 35-CREC18- 0310-016',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Actualizar columnas D, E, F de la hoja resumen de seguimiento de subvenciones',
    'Son los datos numéricos | hoja de seguimiento, hoja de resumen se actualiza solo los € pero los número de expediente NO, ASI QUE PONER A SUMAR (HAY LINEAS YA CON 0 N.º EXPEDIENTES)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar la documentación aportada en platea del expediente 135/1/2022-0516111600',
    'MARIA FERNANDA RUFFINI procedimiento 6951 | NDE: 1L/GDzCB4CdH5+3oBNfyWjbtqoNh/oVzA | Guardarla en \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana\41. 78722097C M. FERNANDA RUFFINI MURIEL (38-CREM22-0039-038) REVISADO    Esto es una prueba',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer tarea 133',
    'Para dia 18/nov.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREM21-0019-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREM21-0029-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREM21-0085-015',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Guardar notificaciones de requerimiento | 12/11/2025 2/6 | llamar a los no notificados, martes día 18.',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\Notificacion_de_requerimiento | Llamar por teléfono. Plazo, desde su publicación. | Enlace tablón, sede electrónica. | Mandar por emial.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Cerrar Seflogic | SUJUP/2010/0000008671 | Ojo, crear un SUDEV | SUDEV/2025/0000000940 | SUDEV/2025/0000000941 | SUDEV/2025/0000000942 | SUDEV/2025/0000000943',
    'Localizar sujup en seflogic arrus cuesta piedra para cerrar con la resolución de SICOIN | Nombre: 2. Resolución Justif SICOIN_PLAN E_02-11-23 | Ruta: \\nieves\ICV_PlA-Exp\Tenerife\Envíos a la ID\RESOLUCIONES ENVIADAS | Subir estas tres cosas: | \\nieves\ICV_PlA-Exp\Tenerife\Envíos a la ID\2. 07-11-2023\Doc Justificativa_PLAN E',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, PUBLICAR en el Tablón de anuncios y notificar a los interesados el REQ_JUSTIF_2019_CONSERV_F',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM21-0029-016',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER\20 ELISA WITTENBACH ESPINO FINALIZADO JUSTIF TOTAL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM21-0019-016',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER\18 MOISES PESTANA SANTANA FINALIZADO JUSTIF TOTAL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM21-0085-015',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER\4 ALEJANDRO RODRIGUEZ DÍAZ FINALIZADO JUSTIF TOTAL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, PUBLICAR en el Tablón de anuncios y notificar a los interesados el REQ_JUSTIF_2019_ACC_F',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expediente de reintegro de: | 38-CREM19-0069-023',
    'Hay que subir toda la documentación de la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\REINTEGROS\Doc reintegros Clara\PR GIULLIANA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expediente de reintegro de: | 38-CREM19-0071-020',
    'Hay que subir TODA la documentación de la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\REINTEGROS\Doc reintegros Clara\PR ELIZABETH',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de requerimiento de justificación de la convocatoria de 2021',
    'Ruta modelo: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Doc.Trabajo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 35-CREC18-0310-016',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\0. FINALIZADOS | Hecha: Ruta de la resolución: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\CONSERVACION | Nombre documento: | RESOL JUST TOTAL TRAS REQU_CONSERV2018_alvarado',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREE19-0029-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/11/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREC18-0410-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('31/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREC18-0372-011',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic del expediente 35-CREC18-0154-016',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Mandar Resolución a NEREIDA,. | NOTA REGIMEN INTERIOR',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\DEVOLUCION J.MANUEL CABRERA MARTIN | concepto modelo 800 erroneo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear el SUDEV, expte:',
    '35-CREM18-0154-021 | SUJUP 2019/4600',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hablar con Patricia sobre el titulo de la resolución.',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\DEVOLUCION J.MANUEL CABRERA MARTIN',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('28/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Buscar la documentación presentada (entre septiembre y octubre de 2025) por Sabina Gorrín Socas',
    'Expediente 38-CREM22-0002-022. Mira en PLATEA y en Hiperreg',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Separar las líneas de SICOIN por provincias para contabilizar el n.º de expedientes por provincias',
    'En el CUADRO DE TRABAJO - SICOIN',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Separar lo que queda pendiente de SICOIN en el cuadro de Wladys por líneas como hicimos con seflogic',
    'Necesito saber n.º de expedientes e importe pendiente de justificar en cada línea',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar e imprimir BOC 103 (mayo 2014) y BOC 145 (julio 2014) HIPOTECA JOVEN 2014',
    'Imprimir y encuadernar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Buscar en hiperreg toda la doc que ha entrado a nombre de RAMOS DE LA CRUZ MARIA CANDELARIA (DNI 43350053K). | jclaher | Viene de la tarea 52, actualziada',
    'Ruta para guardar la documentación: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\ACC2019\38-CREM19-0087-039_RAMOS DE LA CRUZ M CANDELARIA | Guardar la documentación ordenada por fecha | Documentación Guardada en la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\ACC2019\38-CREM19-0087-039_RAMOS DE LA CRUZ M CANDELARIA\Hiperreg_todo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer requerimiento de justificación parcial 38-CREM21-0076-037',
    'Para hacer en septiembre (LA PALMA)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'firmar informe de justificación parcial 38-CREM21-0076-037',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer requerimiento de justificación de los 5 expedientes de 2022 que no han presentado documentación de justificación',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer Resolución',
    'Hacer resolución de justificación después de alegaciones | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\CONSERVACION | Nombre: | RESOL JUST TOTAL TRAS REQU_CONSERV2018_Manuel_Agustin | PENDIENTE A QUE JAVIER HAGA INFORME DE JUSTIFICACIÓN TOTAL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer Resolución',
    'Hacer resolución de justificación después de alegaciones | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\CONSERVACION | Nombre: | RESOL JUST TOTAL TRAS REQU_CONSERV2018_MariaMercedes | PENDIENTE A QUE JAVIER HAGA INFORME DE JUSTIFICACIÓN TOTAL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expedientes reintegro | 9896 procedimiento',
    'Crear expediente de no justificación EFICIENCIA 2018 | 35-CREE18-0023-016 | Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018 | Nombre: | RESOL_NO_JUST_TRAS_REQUERIMIENTO_EFIC_2018_FyR',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expedientes reintegro | 9896 procedimiento',
    'Crar expediente de NO JUSTIFICACIÓN ACC-2018: | 35-CREM18-0166-02 | 35-CREM18-0022-14 | Subir, Resolución de no justificación',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expedientes reintegro | 9896 procedimiento',
    'Crar expediente justificación parcial ACC-2018: | 35-CREM18-0048-008 | Subir, los documentos que están en esta ruta: | gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\REINTEGROS\Doc reintegros Clara',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expedientes reintegro | 9896 procedimiento',
    'Crar expediente justificación parcial ACC-2018: | 35-CREM18-0140-022 | Subir, Resolución de justificación parcial y solicitud de aplazamiento de fecha 29-9-2025',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear expedientes reintegro | 9896 procedimiento',
    'Crar expediente justificación parcial ACC-2018: | 35-CREM18-0053-016 ok | 35-CREM18-0131-016 ok | 35-CREM18-0135-016 ok | 35-CREM18-0182-011 | Solo subir la resolución parcial.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total expediente 35-CREM21-0019-016',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar | Nombre: | Resol_justif_total_35-CREM21-0019-016.pdf',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resoluciones de justificación de los informes de SICOIN con reparos de MUVISA y GRANADILLA',
    '\\nieves\ICV_PlA-Exp\Plan_Accion_Cierre_Exptes\INTERVENCIÓN\Octubre 2025\Documentos sobre reparos\RESOLUCIONES _DE_INFORMES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar respuesta a solicitud',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\José Ramón\Solicitudes\09_10_2025 (Rehabilitación) accesibilidad',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Responder solicitud subvenciones de accesibilidad. Validar hiperreg',
    'C:\Users\dmormarb\Desktop\Diana\Trabajo\Solicitudes\7. 09_10_2025 (Rehabilitación) accesibilidad',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución 1',
    '\\nieves\ICV_PlA-Exp\Plan_Accion_Cierre_Exptes\INTERVENCIÓN\Octubre 2025\Documentos sobre reparos\RESOLUCIONES _DE_INFORMES\Resoluciones para la ID | Nombre: | 1-RESOL_JUSTIF_CAL DEF_SUELO_2005_FyR',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución 2',
    '\\nieves\ICV_PlA-Exp\Plan_Accion_Cierre_Exptes\INTERVENCIÓN\Octubre 2025\Documentos sobre reparos\RESOLUCIONES _DE_INFORMES\Resoluciones para la ID | Nombre: | 2-RESOL_JUSTIF_Autoconstruccion_FyR',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento de expediente 38-CREC18-0257-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\44 ALEMAN IZQUIERDO FCA DOLORES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento de expediente 38-CREM21-0085-031',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\23. 78645339J SAUL BARROSO PÁEZ (38-CREM21-0085-031)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic tarea 117',
    'Esperar a que esté firmada | Ruta: | search-ms:displayname=Resultados%20de%20la%20búsqueda%20en%20%5C%5Cgando%5CCIcvPrvGc%5CPRIVADA%5CRehabilitacion%5C2018%5CEXPEDIENTES%20JAVIER&crumb=location:%5C%5Cgando%5CCIcvPrvGc%5CPRIVADA%5CRehabilitacion%5C2018%5CEXPEDIENTES%20JAVIER\44 ALEMAN IZQUIERDO FCA DOLORES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución expte 35-CREC18-0257-016',
    'Coger ejemplo la resol de justif tras requerimiento expte TIAGUA. En portafirmas el 07-10-2025 | Ruta: | search-ms:displayname=Resultados%20de%20la%20búsqueda%20en%20%5C%5Cgando%5CCIcvPrvGc%5CPRIVADA%5CRehabilitacion%5C2018%5CEXPEDIENTES%20JAVIER&crumb=location:%5C%5Cgando%5CCIcvPrvGc%5CPRIVADA%5CRehabilitacion%5C2018%5CEXPEDIENTES%20JAVIER\44 ALEMAN IZQUIERDO FCA DOLORES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Pedir acceso a PLATEA 9896 (reintegros) a José Ramón',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/10/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del año 2021expte 38-CREM21-0085-031',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\23. 78645339J SAUL BARROSO PÁEZ (38-CREM21-0085-031) | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre: | Resol_justif_total_38-CREM21-0085-031',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Guardar en la carpeta los informes de abono de los expedientes de Javier',
    'Carpeta origen: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2022\02. Expedientes\2. SEFLOGIC | Carpeta destino: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier | 1.- | VINCULADO A TAREA 44',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Confirmar en seflogic si se abonaron las subvenciones de 2022. Si se abonaron hay que localizar la documentación de justificación',
    'SUJUP/2022/0000014170. Cobro y renunció | SUJUP/2022/0000014172 Documentación justificación | SUJUP/2022/0000014047 Cobrado 5/1/2023, no presenta nada | SUJUP/2022/0000014058 cobro | SUJUP/2022/0000014226 cobro y renunció | SUJUP/2022/0000014052 cobro, no presenta nada | Ruta de las carpetas (_sinrevisar) | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer SUDEV Ciempiés y cerrar SUJUP',
    'SUJUP/2023/0000012739 | SUDEV/2025/0000000824',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Subir a PLATEA doc tarea 109',
    'Expediente PLATEA 2/1/2024-0527085235 | pte informatica | Resuelto',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Subir a PLATEA doc tarea 108',
    'Expediente PLATEA 4/1/2023-0622121817 | pte informatica | Resuelto',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar y notificar la resolución de aceptación de renuncia de GEURSA / expt 2024',
    '\\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2024\COHOUSING 2024\RENUNCIA GEURSA | En la misma ruta esta la RfyR y la notificación por sede.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar y notificar la resolución de aceptación de renuncia de Ciempiés / expt. 2023',
    '\\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2023\COHOUSING 2023\RENUNCIA CIEMPIÉS_17-09-25 | En la misma ruta esta la RfyR y la notificación por sede.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Subir a PLATEA el certificado del ministerio de BRISAS firmado y registrado',
    'Expediente PLATEA 5/1/2023-0622121817 | Error, email a informática, pendiente de hablar con Mari',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar certificado BRISAS',
    'Ruta \\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2023\COHOUSING 2023\MINISTERIO | error pte de firma',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Terminar tareas 42 y 44',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2022\02. Expedientes',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar de PLATEA la nueva documentación de GEURSA',
    'Procedimiento 7779, año 2024. Aún no la han presentado, hay que estar pendiente. | Guardarla en la ruta: \\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2024\COHOUSING 2024\3.2. FINALIZACIÓN - JUSTIFICACIÓN\RENUNCIA_GEURSA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar de PLATEA la doc aportada por Ciempiés',
    'Procedimiento 7779, año 2023. | Guardarla en la ruta: \\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2023\COHOUSING 2023\RENUNCIA CIEMPIÉS_17-09-25',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de subvenciones del expte 35-CREM21-0067-006',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de subvenciones del expte 38-CREM21-0045-024',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de subvenciones del expte 35-CREM21-0056-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Buscar las bases de 2017',
    'Ruta \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, actualizar hoja y cerrar seflogic expediente 38-CREM21-0043-023',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\10. 43773382N MARÍA N. RIVERO JORGE (38-CREM21-0043-023) pte devol intereses | OJO SEFLOGIC HAY QUE CREAR UN SUDEV',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic expediente 35-CREE18-0023-016 | Enviar a reintegros y actualizar hoja de seguimiento',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\13 JOSUE MATA MORA EFIC ENERGETICA | (OJO. ES DE NO JUSTIFICACIÓN. IMPORTE JUSTIFICADO = A CERO EN SEFLOGIC)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Enviar a reintegros accesibilidad 2018',
    'Recordar a Patricia que hay que crear la bandeja de hiperreg de reintegros',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar la hoja de subvenciones expte 35-CREM21-0066-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de justificación parcial y aceptación de la devolución voluntaria expte 38-CREM21-0043-023',
    'Hay que subir en seflogic los modelos 800 asociados al sudev',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('08/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Cerrar Seflogic y hoja de seguimiento y enviar a reintegro la tarea 85',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('08/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar cuadro expte (35-CREM21-0102-016)',
    'Ruta resolución firmada: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar el último listado de la intervención sobre SICOIN (agosto2025)',
    'Comprobar si en este listado cerraron los expedientes que ya habíamos enviado | (EXPEDIENTES_REMITIDOS_NOCERRADOS_14-08-2025)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Firmar informe eladio concepcion (La Palma)',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total de los expedientes: | NIEVES MARTÍN (35-CREM21-0056-016) | ASUNCIÓN FERRERA (35-CREM21-0067-006) | 38CREM21-0045-024',
    'Ruta informes: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta resolución: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar | Nombre: | Resol_justif_total_35-CREM21-0056-016. En portafirmas el 15-09-2025 | informe, diana 2021, resolución justificación expt.: 38CREM21-0045-024 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre: | Resol_justif_total_38-CREM21-0045-024. En portafirmas el 15-09-2025 | Resol_justif_total_38-CREM21-0067-006. En portafirmas el 15-09-2025',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de no justificación de 35-CREE18-0023-016 y pasar a reintegros',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\13 JOSUE MATA MORA EFIC ENERGETICA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar cuadro expte 35-CREM21- 0002-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar las resoluciones de justificación parcial y no justificación de accesibilidad 2018 (OJO, las que no marcaron telemático hacerlas en papel)',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar por sede la visita de inspección 35CREC18-00410-016',
    'Ruta del doc a notificar: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\16 CANTERO LLEO MARIA BERTA | Notificada. Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\16 CANTERO LLEO MARIA BERTA | Nombre: | Documento-PUESTA_A_DISPOSICION_NOTIFICACION VISITA INSPECCION_35CREC18-00410-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic (ojo abrir SUDEV) y notificar resolución de GEURSA',
    '\\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2024\COHOUSING 2024\RENUNCIA GEURSA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja subvenciones de expediente 35-CREC19-0341-005',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expediente 35-CREM22-0021-016 (MARTA)',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar la resolución RESOL_NO_JUST_TRAS_REQUERIMIENTO_ACC_2018_F Notificar a cada interesado, cerrar seflogic, actualizar cuadro y remitir expedientes a reintegros',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic (ojo abrir dos SUDEV) y actualizar hoja de seguimiento expediente 35-CREC19-0373-006 (JONÁS)',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\CONSERV_2019',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar la resolución RESOL_JUST_PARCIAL_TRAS_REQUERIMIENTO_ACC_2018_F Notificar a cada interesado, cerrar seflogic, actualizar cuadro y remitir expedientes a reintegros',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic (ojo abrir dos SUDEV) y actualizar hoja de seguimiento expediente 35-CREM21-0030-006 (SYLVIA)',
    'Ruta resolución \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('01/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resoluciones de justificación total de exptes: | 35-CREM21-0002-016 | 35-CREM21-0066-016 | 35-CREM21-0102-016',
    'Informes en \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar | Nombre: | Resol_justif_total_35-CREM21-0002-016 En portafirmas el 04-09-2025. Firmada. Tarea 91 | Resol_justif_total_35-CREM21-0066-016 En portafirmas el 08-09-2025 | Resol_justif_total_35-CREM21-0102-016 En portafirmas el 04-09-2025. Firmada. Tarea 91',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Pasar a la firma resolución firma de just total expediente 35-CREM21-0055-026 NEHALENIA FERNANDEZ SANCHEZ',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER | Nombre: Resol_justif_total_35-CREM21-0055-0261',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('01/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja subvenciones de exptes 35-CREC19-0221-021 y 35-CREC19-0370-005',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Pasar a la firma resol de just total expte 35-CREM22-0075-011',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022 | Nombre: resolucion_justificacion_',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('01/09/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja subvenciones de expte 35-CREM21-0034-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Para pasar a la firma Resolución de justificación total expediente 35-CREM22-0021-016 MARTA HDEZ LLADO',
    'Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022 | Nombre: 35-CREM22-0021-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('29/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Volver a hacer resol de just total expte 35-CREC19-0341-005',
    'Había una errata en el informe técnico con lo cual la fecha del mismo cambia. Hay que cambiar antecente séptimo: la fecha del informe cuando Javier lo modifique. | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES | Nombre: | Resolución_Justificacion_35-CREC19-0341-005',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Terminar Resolución SYLVIA, pte informe Javier',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Doc.Trabajo | Nombre: | RESOL_JUSTIF_Y_DEVOLUCION_TRAS REQUERIMIENTO_2021_sylvia',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('28/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer modelo de notificación de visita de inspección de las convocatorias CONS2018,EFIC2018,ACC2019, CONS2019,EFIC2019,REH2021 y REH2022',
    'Modelo de ejemplo Accesibilidad 2018 (pendiente de corregir por Patricia): \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\ACCESIBILIDAD',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer SUDEV',
    '\nieves\CIcvPrvTf\Privada\COMUN\01_SUBVENCIONES CONCURRENCIA COMPETITIVA\2024\COHOUSING 2024\RENUNCIA GEURSA | SUDEV/2026/0000000208 | SUDEV/2026/0000000209',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('27/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expte 35-CREM21-0034-016',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar | Nombre archivo doc y pdf: | Resol_justif_total_35-CREM21-0034-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de Jonás López Morales',
    'Borrador empezado. Ya devolvió la parte no justificada y los intereses. Incluirlo en borrador',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución justificación total, expte | 35-CREC19-0221-021 | 35-CREC19-0341-005 | 35-CREC19-0370-005',
    'Resoluciones hechas y guardadas en doc y pdf en la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just parcial (comprobar si se hizo requerimiento previo) expte 35-CREM22-0004-016 MOLOWNY PEREZ',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | OJO, hay un escrito pidiendo el cálculo de los intereses (ver correo de Javier el 2/03/2026) Javier le envió el correo???',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('26/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar los modelos de requerimientos de justificación del año 2019',
    'Acc-2019 hecho, pendiente de que Javier termine los informes para el anexo.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('03/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expte 35-CREM22-0075-011',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022 | Nombre: resolucion_justificacion_',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Corregir con Patricia los modelos de just parcial y no justif de accesibilidad 2018',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('02/03/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento de los siguientes expedientes: | 35-CREM22-0102-004 | 35-CREM22-0093-034 | 35-CREM22-0109-026 | 35-CREM22-0029-016 | 35-CREM22-0007-018',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('21/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Rellenar las fechas de abono (seflogic)',
    'Nombre de documento: RESOL_NO_JUST_TRAS_REQUERIMIENTO_ACC_2018 | Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\ACCESIBILIDAD',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total expediente 35-CREM22-0021-016 MARTA HDEZ LLADO',
    'Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022 | Nombre: 35-CREM22-0021-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar y notificar Resolución de denegación de prorroga 35-CREE19-0018-016). OJO. NO CERRAR SEFLOGIC.',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\EFICIENCIA_CREE19\35-CREE19-0018-016 (Solicitud prórroga)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Urgente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar entradas hiperreg. Revisar entradas a PLATEA',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer listado wlady solo pendientes de enviar.',
    'Hacer listado wlady solo pendientes de enviar. | Guardar como PENDIENTE_DE_ENVIO_14-08-25',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Descargar justificantes intereses GEURSA, hacer resol de acept y archivar expediente de reintegro',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Rellenar columna FECHA DE ABONO y fundamento de derecho DÉCIMO en la RESOL JUST PARCIAL TRAS REQUER CONSERVACIÓN',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\CONSERVACION',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de just total expediente 35-CREM21-0055-026 NEHALENIA FERNANDEZ SANCHEZ',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\JAVIER | Nombre: Resol_justif_total_35-CREM21-0055-0261',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de subvenciones de exptes. | 35-CREM21-0008-016 | 35-CREM21-0001-016 | 35-CREM21-0044-022 | 35-CREM21-0009-021',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expediente 35-CREM22-0007-018 JOSE LUIS SANTAMARIA DE LA MATA',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar erratas de texto e importes resolución denegación de prórroga',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\EFICIENCIA_CREE19\35-CREE19-0018-016 (Solicitud prórroga)\Modelos | RESOLUCIÓN DE DENEGACIÓN DE PRÓRROGA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expediente 35-CREM22-0102-004 JUAN TOMAS PEREZ HDEZ',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de subvenciones de exptes. 38-CREM21-0070-038 y 38-CREM21-0087-038',
    'Ruta \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expediente 35-CREM22-0093-034 ROSA MARIA MARTIN',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('07/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar resolución de justificación total de los expedientes de la tarea 62',
    '38-CREM21-0070-038 y 38-CREM21-0087-038 | Ruta informes: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana | Resoluciones hechas pendientes de subir a la firma. En portafirmas el 11/08/2025 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Nombres: | Resol_justif_total_38-CREM21-0070-038.pdf | Resol_justif_total_38-CREM21-0087-038.pdf',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expediente 35-CREM22-0029-016 RAFAEL GÓMEZ ROMERO',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar y notificar la contestación a las alegaciones de Berta',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018 | NOMBRE DOCUMENTO: RESOL_Alegaciones_35-CREC18-0410-016_F',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total expediente 35-CREM22-0109-026 MARÍA DOLORES',
    'Ruta informe \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Firmar informes técnicos expedientes rehabilitación 2021 nº 17 y nº 24.',
    'Ruta informes: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Terminar cronograma del Plan de Acción',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de resolución de justificación total de expediente 38-CREM21-0072-024 (tarea 51)',
    'Ok, ya esta firmado',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Enviar a la ID autoconstrucción',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de resolución de justificación total de expediente 38-CREM21-0080-024 (tarea 50)',
    'Ok, ya esta firmado',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Publicar requerimiento de VU en el Tablón',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/08/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de resolución de justificación total de expediente 38-CREM21-0047-027 (tarea 49)',
    'Ok, ya esta firmado',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar y notificar a cada uno el requerimiento de Vivienda usada',
    'Ruta requerimiento: \\nieves\ICV_PlA-Exp\2026\SICOIN\Documentos de trabajo\Vivienda Usada',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Cuadro pendiente de sumas remitidos / pendiente intervención',
    'Ruta: | \\nieves\ICV_PlA-Exp\JoseRamon | Nombre: | cuadro pendiente revisar 30-9-2024_Wlady_filascoinciden',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('19/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución. Notificar, actualizar hoja de seguimiento y cerrar seflogic',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones para registrar | OJO. Hay que crear dos SUDEV',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Cuadro Wlady, cuadro intervención',
    'Borrador escrito para la intervención: | Ruta: | \\nieves\ICV_PlA-Exp\Modelos | Nombre: | Oficio envío ID_reiteración de expedientes ya enviados | JCLA_Oficio envío ID_reiteración de expedientes ya enviados | Cuadro resumen Ruta: | \\nieves\ICV_PlA-Exp\Plan_Accion_Cierre_Exptes\INTERVENCIÓN | Nombre: | Filas_Extraidas_Final_24_07_2025',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar oficio de envío a la ID de autoconstrucción',
    'Ruta modelo: \\nieves\ICV_PlA-Exp\2026\SICOIN\Documentos de trabajo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hoja de tareas | jclaher',
    'Cambiar el orden es decir la primera de todas la más reciente y la ultima la número 1',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de SICOIN Autoconstrucción',
    'Ruta de resolución firmada: \\nieves\ICV_PlA-Exp\2026\SICOIN\Documentos de trabajo\Autoconstrucción',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'R.E. 1355884/2025 | h76582279',
    'Planos de los Realejos, pendiente de Miguel del archivo. Scanear en Jorge y remitir con un recibi de pdf. | Mande un WhatsApp a Díana',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('12/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Asignar grupos de usuarios a los expedientes de reintegros ya creados',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'R.E. 560279',
    'Buscar donde esta esta entrada y tramitar. Llega la información de un email a Diana | Noelia no encuentra nada con esa anotación y yo tampoco, pendiente de consultar el emial. | Se queda sin acción administrativa hasta que se sepa que es',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('11/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Publicar en el Tablón de Anuncios del ICV el requerimiento de justificación de 2022',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    '35-CREC18-0154-016',
    'Buscar el abono de la justificación, ojo abono en efectivo y debe de ser en transferencia 3000 | DNI: 42864107L | Hiperreg no deja (doc. fisica), en carpetas solo veo una factura donde no consta la forma de pago. No veo documento de transferencia. | Ruta factura: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\54 PEREZ DORESTE MERECEDES\42864107L\DOCUEMNTOS SEPTIEMBRREÇ',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('11/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de requerimiento de justificación 2022',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Buscar en hiperreg toda la doc que ha entrado a nombre de RAMOS DE LA CRUZ MARIA CANDELARIA (DNI 43350053K). | jclaher',
    'Ruta para guardar la documentación: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\ACC2019\38-CREM19-0087-039_RAMOS DE LA CRUZ M CANDELARIA | Guardar la documentación ordenada por fecha | Documentación Guardada en la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\ACC2019\38-CREM19-0087-039_RAMOS DE LA CRUZ M CANDELARIA\Hiperreg_todo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Mirar en hiperreg si ha entrado doc después del 10 de noviembre de 2025 del expediente 35-CREM21-0093-001',
    'DNI 43295254P | RAÚL MANUEL DÁMASO SUÁREZ | No ha presentado nada',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total de expediente 38-CREM21-0072-024',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\18. 42154737S JUAN RAMÓN GONZALEZ (38-CREM21-0072-045) LA PALMA_Informe listo | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_38-CREM21-0072-045',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Mirar en hiperreg si ha entrado doc después del 30 de diciembre de 2025 del expediente 35-CREM21-0054-016',
    'DNI 42821018D | RITA SOSA MARTÍN | No ha presentado nada',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total de expediente 38-CREM21-0080-024',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\21. 42236853K JUAN E. CACHES(38-CREM21-0080-024) LA PALMA_Informe listo | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_38-CREM21-0080-024',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Urgente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 35-CREM21-0040-019. | Hay que hacer dos SUDEV',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Resoluciones firmadas para registrar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('22/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total de expediente 38-CREM21-0047-027',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\12. 42148233C CARMEN ROSA FDEZ PERERA (38-CREM21-0047-027) LA PALMA_Informe listo | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_38-CREM21-0047-027',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 35-CREM22-0097-002',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('21/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar respuesta de solicitud REG546551',
    '\\nieves\ICV_PlA-Exp\JoseRamon\REGISTRAR-NOTIFICAR | documentación Ruta: | \\nieves\ICV_PlA-Exp\JoseRamon\REGISTRAR-NOTIFICAR\SOLICITUD_REG546551',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 35-CREC19-0278-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Llamar al ayuntamiento de Puntagorda para expediente 38-CREM21-0022-029',
    'El beneficiario vendió la casa. Información sobre los nuevos propietarios',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 35-CREM22-0009-021',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer requerimiento de justificación parcial 38-CREM21-0076-037',
    'Para hacer en septiembre (LA PALMA)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 35-CREM22-0013-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer informe de justificación parcial 38-CREM21-0076-037',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte. 38-CREM21-0089-008',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Resoluciones firmadas para registrar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar la documentación de justificación de los expedientes pendientes de Javier del año 2022',
    'Replicar lo que hice yo con los míos | Ruta de ejemplo: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Diana | Ruta para reproducir las carpetas: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier | Ruta: de los expedientes justificaciones: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2022\08. JUSTIFICACIONES | Hacer lo mismo que diana en una carpeta de javier 2022 para tener solo los expedientes de las palmas de 2022 que junto con los de Diana que son 21 sería el total.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte 35-CREM19-0093-012. Crear expediente de reintegro',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\ACC2019\Resoluciones para registrar | OJO. ES JUSTIFICACIÓN PARCIAL. HAY QUE ABRIR PROC REINTEGRO DE LA PARTE QUE NO JUSTIFICA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar modelo de Informe Técnico y de correo para visita para las subvenciones de rehabilitación 2022',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Modelos',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('06/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar, cerrar seflogic y actualizar hoja de seguimiento expte 38-CREM21-0062-038',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Resoluciones firmadas para registrar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Rellenar columnas de la M a la S de la pestaña 2022 de la hoja de subvenciones',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana. Debería haber 21 expedientes míos y el resto de Javier | IMPORTANTE: O se rellena la coliumna R o la S, no son compatibles. Rellenar todos los datos desde la M HASTA LA Q | LIO No veo nada en 3 expte. Y no hay nada en carpeta de javier., PARA VERLO CON DIANA: | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana | Nombre: | columna RyS_ hoja_Seguimiento Subvenciones',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('05/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total tras requerimiento 35-CREC19-0278-016 (MARIUCHA)',
    'Ruta informe (COGER EL FAVORABLE): \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\CALCULO_C_PRP_MARIUCHI',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar requerimiento de los expedientes de 2021 ilocalizables',
    'n.º49 y 60 ( modelo de requerimiento 2018 y prepararlo) Mirar informe visita o no presentan HIPERREG, para hacer en septiembre.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de justificación total expediente 35-CREM22-0097-002 | RODRIGUEZ RODRIGUEZ, MARIO DE JESÚS',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | Ruta resolución hecha: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Programar visita expedientes pendientes 2021 (6 expedientes)',
    'Falta enviar correos de visita a: | 38-CREM21-0085-031 | 38-CREM21-0082-038',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de justificación total expediente 35-CREM22-0013-016 | MARIA VICTORIA MONTESDEOCA TROYA',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS | Ruta resolución hecha: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Llamar a la beneficiaria del expediente 38-CREM21-0043-023 para la devolución de los intereses',
    'Ruta expediente. Ver informe (documento IT): | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\10. 43773382N MARÍA N. RIVERO JORGE (38-CREM21-0043-023) VISITADO | COMPROBAR QUE SE HA REALIZADO EL INGRESO DE LOS INTERESES EN HIPERREC y si no preguntar a la señora que paso. | RESPUESTA: | A la fecha 31/07/2025, la señora telefónicamente me informa que no ha realizado el ingreso del modelo 800 por estar ocupada por una situación personal. Se le informa que una vez que lo realice lo comunique por email a la encargada de la Linea, que ella reconoce conocer su emial y su nombre.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Mirar en hiperreg si ha llegado la devolucion de los INTERESES del expediente 35-CREM21-0040-019 | Hacer resol de acept y just',
    'Importe de los intereses: 539,23 € | Si no ha llegado llamarlo porque según un correo suyo ya los devolvió (Saagar Vatnani 665 833 436) | Descargada documentación, devolución intereses.Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Requerimiento de justificación\RESPUESTA A REQUERIMIENTOS\35-CREM21-0040-019_SAAGAR VATNANI VATNANI',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar legislación SICOIN expedientes de devoluciones',
    'Todos los anteriores a dic de 2010 son diferentes en cuanto a los intereses (ley de hacienda canaria). En esos casos incluir en normativa la ley de presupuestos del año del cálculo de intereses',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Comprobar cuántos expedientes de inquilino de las palmas están revisando a la semana. Hacer previsión por equipos de trabajo',
    'Verlo con David en septiembre',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación parcial tras requerimiento expediente 35-CREM19-0093-012',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\Requerimiento de justificación\CONTESTACION REQUERIMIENTO\35-CREM19-0093-022_PEDRO GIL RIVERO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Preparar la respuesta al requerimiento de justificación/subsanación 2018 de los que no contestaron',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. Trabajo | ACC HECHO. Solo anexo II | Conservación, ok texto resolución, pendiente tabla | Eficiencia, sin hacer',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('04/02/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de just total 35-CREM22-0009-021',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS. | Ruta resolución hecha: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación 35-CREM21-0009-021',
    'Ruta informe: | Gando\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_35-CREM21-0009-021',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Actualizar el borrador del Plan de cierre con los nuevos datos de la ID',
    'Ruta últimos datos: \\nieves\ICV_PlA-Exp\2026\Intervención',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación 35-CREM21-0008-016',
    'Ruta informe: | Gando\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_35-CREM21-0008-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Crear documento para 2026 de resumen de expedientes remitidos a la ID',
    'Guardarlo en la ruta:\\nieves\ICV_PlA-Exp\2026\Documentos de trabajo',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación 35-CREM21-0001-016',
    'Ruta informe: | Gando\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_35-CREM21-0001-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de just total 35-CREM21-0095-024. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Resoluciones firmadas para registrar | Registrada: | Resol_justif_total_35-CREM21-0095-024_FyR | Notificada | self',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación 35-CREM21-0044-022',
    'Ruta informe: | Gando\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar\PTE DE REVISAR | Documento y pdf: | Resol_justif_total_35-CREM21-0044-022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución SICOIN 38-SG-19/07',
    'Ruta: \\nieves\ICV_PlA-Exp\2026\Suelo VPO\7. ROYCASA | hecho en la misma ruta.',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer un repaso con Javier de los exptes pendientes 2018 y 2019',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de just total 35-CREM22-0022-002. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar) | Notificada | sefl',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/07/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de la tarea 27',
    'Ruta resolución firmada: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\20. 43824922D EDGAR LUIS (38-CREM21-0079-023) VISITADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de just total 35-CREM22-0026-002. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar) | Notificada | sefl',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Ver qué pasó con los expedientes de las tareas 3 y 4',
    'El representante de Pedro de la Nuez presentó una queja formal porque notificamos al interesado y no al representante pero en la hoja de seguimiento no veo ninguna nota de haberle notificado. He encontrado la resolución de justificación en la ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019 y he notificado al representante. | Hay que comprobar si la resolución de justificación se subió a seflogic, cerrar el expediente y actualizar la hoja de seguimiento. Lo mismo con el de la tarea 4. Cada vez que notifiquemos mirar si hay representante y notificar a ambos de ahora en adelante. | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana | Nombre archivo: que paso tarea 3y4.doc',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de just total 35-CREM22-0099-020. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar) | Notificada | sefl',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('30/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Ordenar cronológicamente los documentos de los expedientes que van a ir a reintegros para que el departamento de reintegros pueda crearlos en PLATEA',
    'Expedientes: 35-CREM18-0053-016, 35-CREM18-0131-016, 35-CREM18-0135-016, 35-CREM18-0140-022, | 35-CREM18-0154-021, 35-CREM18-0166-002, 35-CREM18-0182-011, 35-CREM18-022-014, 35-CREC18-0154-016, 35-CREC18-0257-016, 35-CREC18-0372-011, 35-CREC18-0410-016 | Guardarlos en la carpeta PARA REMITIR A REINTEGROS. Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018 | Expedientes guardados en la siguiente ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\REINTEGROS\Expedientes_para_reintegro_2018',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resol de just total 35-CREM22-0070-004. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar) | Notificada | seff',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('27/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar en seflogic tarea 19',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\34 COM PROP ED TIAGUA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resol de just total 38-CREM22-0069-020. Notificar, cerrar seflogic y actualizar hoja de seguimiento',
    'Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones firmadas (para registrar) | sef',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('26/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 38-CREM21-0079-023',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\20. 43824922D EDGAR LUIS (38-CREM21-0079-023) VISITADO | Ruta Resolución doc: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre archivo: | Resol_justif_total_38-CREM21-0079-023.doc | Ruta resolución pdf: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre archivo pdf: | Resol_justif_total_38-CREM21-0079-023.pdf',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total TRAS REQUERIMIENTO expte 38-CREM21-0062-038',
    'Ruta informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\15. 54217395R RUTH MERY MUÑOZ FUENTES (38-CREM21-0062-038)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('25/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Notificar carta',
    'Tarea 16, ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\José Ramón | Nombre archivo:',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución SLKPM',
    'Ruta: \\nieves\ICV_PlA-Exp\2026\Suelo VPO\6. SLKPM | Registrada, en la misma ruta, nombre: | 3.-RESOL_JUSTIF_CAL DEF_SLKPM_FyR',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de tarea 20',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\26 COM PROP EDIF 29 ABRIL Nº74',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar facturas ruth mary muñoz',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de tarea 14',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\16. 78854941Q DANIEL BARROSO GARCÍA (38-CREM21-0068-038) VISITADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Para pasar a la firma',
    'Resoluciones pdf. | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Resoluciones de justificacion total\Resoluciones_individuales_favorables_2022 | - 38-CREM22-0069-020 | - 35-CREM22-0099-020 | - 35-CREM22-0026-002 | - 35-CREM22-0022-002 | - 35-CREM22-0070-004',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de tarea 13',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\9. 41842028Z EPIFANIO OSCAR RODRIGUEZ(38-CREM21-0039-038) VISITA 17-06-25 1100h',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 35-CREM22-0070-004',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2022',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('24/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic de tarea 10',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\5. 41857120H ADOLFO FLORES FLORES (38-CREM21-0008-051) VISITADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total del expediente 35-CREM21-0095-024',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\GERMÁN MARTÍN CÁCERES | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\Resoluciones de justificacion para tramitar\Subir a la firma | nombre: | Resol_justif_total_35-CREM21-0095-024',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Copia en escritorio José Ramón hoja Marta.',
    'Pasado al cuadro',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total expediente 35-CREM21-0089-008',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\EXPEDIENTES JAVIER 2021\MARÍA DEL CARMEN GONZÁLEZ GUERRA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Subir resolución al portafirmas',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\26 COM PROP EDIF 29 ABRIL Nº74 | Nombre: RESOL JUST TOTAL TRAS REQU_CONSERV2018_35-CREC18-0145-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Leer bases otras subvenciones recibidas por 35-CREM22-0100-005 y 35-CREM22-0027-019',
    'Ver correo de Javier de 14/01/2026. | Pendiente a que la empresa instaladora (es la misma en los dos casos me llame)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución',
    'Informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\34 COM PROP ED TIAGUA Modelo de resolución en NORA: Tarea 7, fecha cuando contesto el requerimiento. | Ruta resolución:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. trabajo\CONSERVACION | Nombre archivo:RESOL JUST TOTAL TRAS REQU_CONSERV2018_Tiagua',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de EMPRESA PÚBLICA DE LOS REALEJOS',
    '\\nieves\ICV_PlA-Exp\2026\Suelo VPO\1. EMP PÚBLICA LOS REALEJOS',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución, notificar y cerrar seflogic expte 35-CREC18-0227-016',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\48 FRANKEL PINELLI NORA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de MUVISA',
    '\\nieves\ICV_PlA-Exp\2026\Suelo VPO\3. MUVISA\MUVISA 36 VDAS',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('23/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución, notificar y cerrar seflogic expte 35-CREE19-0060-008',
    'RUTA: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\24. SERGIO DE JESUS RODRIGUEZ HERNANDEZ',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('20/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar resolución de SAIRAD',
    '\\nieves\ICV_PlA-Exp\2026\Suelo VPO\4. SAIRAD',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Contestar solicitud ayudas rehabilitación Hiperreg',
    'Correo a Patricia el 23 de junio de 2026',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('19/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'REVISAR AUP LA LAGUNA',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'QUITAR RESOL, art. 37.7',
    'De todos los modelos, es anticipo y no va',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('19/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'SUBIR A LA FIRMA',
    'Ruta: | \\nieves\ICV_PlA-Exp\2026\Suelo VPO\6. SLKPM | Nombre: | 3.-RESOL_JUSTIF_CAL DEF_SLKPM',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justitificación total EXPTE 38-CREM21-0068-038',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\16. 78854941Q Daniel Barroso Garcia(38-CREM21-0068-038) VISITA 17-06-25 0900h | Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre Archivo:Resol_justif_total_38-CREM21_38-CREM21-0068-038',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('19/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'REVISAR RESOLUCIÓN SUELO 2026',
    'Ruta: | \\nieves\ICV_PlA-Exp\2026\Suelo VPO\6. SLKPM | Nombre: | 3.-RESOL_JUSTIF_CAL DEF_SLKPM',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('18/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justitificación total EXPTE 38-CREM21-0039-038',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\9. 41842028Z EPIFANIO OSCAR RODRIGUEZ(38-CREM21-0039-038) VISITA 17-06-25 1100h | Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre Archivo:Resol_justif_total_38-CREM21_38-CREM21-0039-038',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('19/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente de firma'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Carpeta hiperreg pendiente validada',
    'Carpeta escritorio jrc',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic tarea 1',
    'Ruta:\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\7. 45703852T ROBERTO CARLOS MELO LOPEZ(38-CREM21-0028-001) VISITADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Entrada, solicitud pidiendo información sobre subvenciones.',
    'Solicitud a nombre de JESUS ALONSO ALMARAZ | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\SOLICITUDES | Nombre: | Solicitud_Jesus_Alonso_9-1-2026_Entrada_36214.zip',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic tarea 9',
    'Ruta: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\8. 45729691X JACOB DONATE(38-CREM21-0036-017) 10-06-25-0900h VISITADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Mirar en hiperreg si ha entrado la representación de la CP Rialto',
    'Expediente 35-CREC18-0174-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('17/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justitificación total EXPTE 38-CREM21-0008-051',
    'Ruta Informe: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\5. 41857120H ADOLFO FLORES FLORES (38-CREM21-0008-051) VISITADO | Ruta resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar | Nombre Archivo: Resol_justif_total_38-CREM21-0008-051',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM22-0026-002',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justitificación total EXPTE 38-CREM21-0036-017',
    'RUTA INFORME: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\8. 45729691X JACOB DONATE(38-CREM21-0036-017) 10-06-25-0900h | hacer la resolución doc. trabajo 2021 diana. | Ruta resolución: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM22-0022-002',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justitificación total EXPTE 35CREE19-0060-008',
    'RUTA INFORME: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\EFICIENCIA ENERGETICA 2019 | Ruta Archivo: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2019\EFICIENCIA_CREE19\Resoluciones_Justificacion_TRAMITACION | Nombre Archivo: | RESOLUCIÓN JUSTIFICACIÓN TOTAL_35-CREE19-0060-008 | pdf creado: | RESOLUCIÓN JUSTIFICACIÓN TOTAL_35-CREE19-0060-008',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resol de just total del expediente 35-CREM22-0099-020',
    '\\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2022\Expedientes Javier\0. INFORMES TÉCNICOS FINALIZADOS',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('13/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total | EXPTE 35-CREC18-0227-016',
    'Hay que añadir en el antecedente el requerimiento que se hizo y la contestación. Lo hacemos juntos el lunes | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\Doc. Trabajo | Nombre archivo: | RESOL JUST TOTAL TRAS REQU_CONSERV2018_Nora | Ruta Resolución PDF: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2018\EXPEDIENTES JAVIER\48 FRANKEL PINELLI NORA',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('16/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer oficio SICOIN para envío enero 2026',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('11/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Seflogic'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar, notificar y cerrar seflogic',
    'Resoluciones de las tareas 3 y 4',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente de firma'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Entrada, escrito stdo. Resolución',
    'Solicita copia y nombre de personas con resolución Comunidad de Propietarios EDIF. RIALTO, expte.: 35-CREC18-0174-016 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2018\35-CREC18-0174-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('11/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer modelo de resolución de justificación total de eficiencia 2019',
    'Modelo de Resolución realizado. | Ruta Archivo: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\MODELOS PATRICIA\EFICIENCIA (CREE19)',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('15/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Pendiente de firma'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Entrada respuesta requerimiento',
    'Respuesta requerimiento expte.: 35-CREM21-0055-026 | Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Requerimiento de justificación\RESPUESTA A REQUERIMIENTOS\35-CREM21-0055-026_NEHALENIA FDEZ',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total | EXPTE 35-CREC19-0200-016',
    'Ruta informe y modelo de resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019 | Ruta resolución: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES | Ruta Archivo: | RESOLUCIÓN JUSTIFICACIÓN TOTAL_35-CREC19-0200-016',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('14/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Otros'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar hiperreg',
    '',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón / Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total | EXPTE 35-CREC19-0223-033',
    'Ruta, informe y modelo de resolución: \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019 | Ruta resolución: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\2019\EXPTE JAVIER 2019\0. INFORMES TECNICOS FINALIZADOS Y FIRMADOS\CONSERVACION 2019\RESOLUCIONES | Archivo: | RESOLUCIÓN JUSTIFICACIÓN TOTAL_35-CREC19-0223-033',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('14/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar la resolución de SICOIN RESOL_RENUNCIA Y DEV_VOL_MESA_Y_ROSADO_F',
    'Ruta: \\nieves\ICV_PlA-Exp\2026\Suelo VPO\MESA Y ROSADO',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('10/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Revisar uno a uno los BOC de los antecedentes de la Resolución de la tarea anterior',
    'Ruta: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Doc.Trabajo | Archivo: | normativa resolucion CREM21-hay-errores',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('14/01/2026', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Sicoin'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Jose Ramón'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Registrar la resolución de SICOIN | RESOL_JUST_38-SS-007-06-35_SOC_MUN_S_MIGUEL_F',
    'Ruta: \\nieves\ICV_PlA-Exp\2026\Suelo VPO\SOC MUN S MIGUEL',
    TRUE
);

INSERT INTO db_admongral.gestor_tareas_tbtareas (
    fecha,
    id_estado,
    prioridad,
    id_ambito,
    id_tecnico,
    id_grupo,
    titulo,
    descripcion,
    activa
)
VALUES (
    TO_DATE('09/06/2025', 'DD/MM/YYYY'),
    (SELECT id_estado FROM db_admongral.gestor_tareas_tbestados WHERE nombre = 'Completada'),
    'Normal',
    (SELECT id_ambito FROM db_admongral.gestor_tareas_tbambitos WHERE nombre = 'Rehabilitacion'),
    (SELECT id_tecnico FROM db_admongral.gestor_tareas_tbtecnicos WHERE nombre = 'Diana'),
    (SELECT id_grupo FROM db_admongral.gestor_tareas_tbgrupos WHERE nombre = 'General'),
    'Hacer resolución de justificación total',
    'Ruta informe: | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\7. 45703852T ROBERTO CARLOS MELO LOPEZ(38-CREM21-0028-001) VISITADO | Ruta resolución | \\gando\CIcvPrvGc\PRIVADA\Rehabilitacion\Diana\2021\Expedientes pendientes Diana\Resoluciones de justificación para tramitar',
    TRUE
);

COMMIT;
