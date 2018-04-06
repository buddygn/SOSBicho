function confirm_inative(x) {
   if (confirm('Deseja desativar o usuário? '+x)) {
       yourformelement.submit();
   } else {
       return false;
   }
}
