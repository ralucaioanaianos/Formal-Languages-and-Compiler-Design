package ro.ubb.lab11.core.service;


import ro.ubb.lab11.core.model.Airplane;

import java.util.List;

public interface IAirplaneService {
    List<Airplane> getAllAirplanes();
    Airplane addAirplane(String model, int capacity, String registration, int fabricationYear);
    void deleteAirplane(Long id);
    Airplane updateAirplane(Long id, String model, int capacity, String registration, int fabricationYear);
    List<Airplane> findAirplanesByModel(String model);
    List<Airplane> findAllByOrderByAgeAsc();
}
