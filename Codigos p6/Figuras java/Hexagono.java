class Hexagono extends Figura {
    private double lado;

    public Hexagono(double lado) {
        this.lado = lado;
    }

    @Override
    public double calcularArea() {
        return (3 * Math.sqrt(3) * Math.pow(lado, 2)) / 2;
    }

    @Override
    public double calcularPerimetro() {
        return 6 * lado;
    }
}