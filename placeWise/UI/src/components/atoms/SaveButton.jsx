const SaveButton = ({ onClick }) => (
    <button
      className="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded mr-2"
      onClick={onClick}
    >
      Guardar cambios
    </button>
  );
  
  export default SaveButton;