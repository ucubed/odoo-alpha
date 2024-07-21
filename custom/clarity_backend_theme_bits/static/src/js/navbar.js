/** @odoo-module **/

import { NavBar } from '@web/webclient/navbar/navbar';
import { useService, useBus } from '@web/core/utils/hooks';
import { patch } from "@web/core/utils/patch";
import { useEnvDebugContext } from "@web/core/debug/debug_context";
 
patch(NavBar.prototype, {
    setup() {  
        super.setup(); 
        this.debugContext = useEnvDebugContext();
        this.rpc = useService('rpc');
        this.companyService = useService("company");
        this.currentCompany = this.companyService.currentCompany;
        this.menuService = useService("menu");  
    },
    toggleSidebar(ev){  
        $(ev.currentTarget).toggleClass('visible');
        $('.nav-wrapper-bits').toggleClass('toggle-show');
    },  
});