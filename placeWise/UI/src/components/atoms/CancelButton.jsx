const CancelButton = ({ onClick }) => (
    <button
      className="bg-red-700 hover:bg-red-900 text-white font-bold py-2 px-4 rounded mr-10"
      onClick={onClick}
    >
      Cancelar
    </button>
  );
  
  export default CancelButton;