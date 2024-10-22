/** @odoo-module **/

/*
 *
 * (c) Copyright Ascensio System SIA 2024
 *
*/

import { patch } from "@web/core/utils/patch";
import { DocumentsInspector } from '@documents/views/inspector/documents_inspector';
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

const oo_editable_formats = [
    "docx",
    "xlsx",
    "pptx",
    "pdf",
]

const oo_viewable_formats = [
    "djvu",
    "doc",
    "docm",
    "docxf",
    "dot",
    "dotm",
    "dotx",
    "epub",
    "fb2",
    "fodt",
    "html",
    "mht",
    "odt",
    "ott",
    "oxps",
    "rtf",
    "txt",
    "xps",
    "xml",
    "csv",
    "fods",
    "ods",
    "ots",
    "xls",
    "xlsb",
    "xlsm",
    "xlt",
    "xltm",
    "xltx",
    "fodp",
    "odp",
    "otp",
    "pot",
    "potm",
    "potx",
    "pps",
    "ppsm",
    "ppsx",
    "ppt",
    "pptm",
];

patch(DocumentsInspector.prototype, {
    setup() {
        super.setup(...arguments);
        this.notification = useService("notification");
        this.onlyofficeEditorUrl = this.onlyofficeEditorUrl.bind(this);
    },
    showOnlyofficeButton(records) {
        if (records.length !== 1) return false;
        const ext = records[0].data.display_name.split('.').pop()
        return records.length === 1 && 
            (this.onlyofficeCanEdit(ext) || this.onlyofficeCanView(ext));
    },
    onlyofficeCanEdit(extension) {
        return oo_editable_formats.includes(extension);
    },
    onlyofficeCanView(extension) {
        return oo_viewable_formats.includes(extension);  
    },
    async onlyofficeEditorUrl(id) {
        var demo = await this.env.services.orm.call('ir.config_parameter', 'get_param', ['onlyoffice_connector.doc_server_demo']);
        var demoDate = await this.env.services.orm.call('ir.config_parameter', 'get_param', ['onlyoffice_connector.doc_server_demo_date']);
        demoDate = new Date(Date.parse(demoDate))
        if (demo && demoDate && demoDate instanceof Date) {
            const today = new Date();
            const difference = Math.floor((today - new Date(Date.parse(demoDate))) / (1000 * 60 * 60 * 24));
            if (difference > 30) {
                this.notification.add(
                    _t(
                        "The 30-day test period is over, you can no longer connect to demo ONLYOFFICE Docs server"
                    ),
                    {
                        title: _t("ONLYOFFICE Docs server"),
                        type: 'warning',
                    }
                );
                return;
            }
        }
        window.open(`/onlyoffice/editor/document/${id}`, '_blank');
    }
});